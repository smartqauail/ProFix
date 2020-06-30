from django.urls import reverse
from django.shortcuts import render, redirect
from Avadell.models import Cotizacion,InvoiceItem
from .forms import CotizacionCreateForm
from cart.cart import Cart
from .tasks import invoice_created
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import get_object_or_404
from Avadell.models import Cotizacion,InvoiceItem
from profixprojects.models import Project,mantenimiento
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.core.files.storage import FileSystemStorage
from django.utils.translation import gettext_lazy as _

from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer,Image 
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch

from datetime import datetime, date
from profixinvoice.models import InvoiceInfo, ServiceProviderInfo, ClientInfo, Item, Transaction
from profixinvoice.templates import SimpleInvoice



def invoice_created(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = CotizacionCreateForm(request.POST)

        if form.is_valid():
            cotizacion = form.save(commit=False)
            if cart.coupon:
                cotizacion.coupon = cart.coupon
                cotizacion.discount = cart.coupon.discount
            cotizacion.save()

            for item in cart:
                InvoiceItem.objects.create(cotizacion=cotizacion,
                                         project=item['project'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            # clear the cart
            cart.clear()
            # launch asynchronous task
            invoice_created.delay(Cotizacion.id)
            # set the order in the session
            request.session['cotizacion_id'] = Cotizacion.id
    
            # redirect for payment
            return redirect(reverse('payment:process'))
    else:
        form = CotizacionCreateForm()
    return render(request,
                  'Avadell/cotizacion/create.html',
                  {'cart': cart, 'form': form})


@staff_member_required
def admin_cotizacion_detail(request, cotizacion_id):
    cotizacion = get_object_or_404(Cotizacion, id=cotizacion_id)
    return render(request,
                  'admin/avadell/cotizacion/detail.html',
                  {'Cotizacion': Cotizacion})


@staff_member_required
def admin_cotizacion_pdf(request, cotizacion_id):
    cotizacion = get_object_or_404(Cotizacion, id=cotizacion_id)
    #paid = get_object_or_404(Order, paid=order.paid)
    #name  = get_object_or_404(Order, first_name=order.first_name)
    #address  = get_object_or_404(Order, address=order.address)

    html = render_to_string('Avadell/cotizacion/pdf.html',
                            {'Cotizacion': Cotizacion})
                            
    doc = SimpleInvoice("/tmp/cotizacion_{}.pdf")
   
    
    #doc.is_paid = order.paid # Paid stamp, optional
    doc.invoice_info = InvoiceInfo(cotizacion.id, cotizacion.created , cotizacion.updated)  # Invoice info, optional
    
    # Service Provider Info, optional
    doc.service_provider_info = ServiceProviderInfo(
    name='Maria Fernanda', 
    street = 'Edificio Avadell' ,
    city= '',
    post_code='222222',
    state= '',
    country='My Country',
    vat_tax_number='Vat/Tax number',
    email='',
   
    )
   

# Client info, optional
    doc.client_info = ClientInfo(
    email='client@example.com',
    name= '',
    provider='fasfas'
    )

# Add Item
    doc.add_item(Item('saaa', 'dsd', 1, '1.1'))
    doc.add_item(Item('Item', 'Item desc', 2, '2.2'))
    doc.add_item(Item('Item', 'Item desc', 3, '3.3'))

# Tax rate, optional
    doc.set_item_tax_rate(20)  # 20%

# Transactions detail, optional
    doc.add_transaction(Transaction('Paypal', 111, datetime.now(), 1))
    doc.add_transaction(Transaction('Stripe', 222, date.today(), 2))

# Optional
    doc.set_bottom_tip("Email: example@example.com<br />Don't hesitate to contact us for any questions.")

    doc.finish()
    
    #response = HttpResponse(content_type='application/pdf')
    #response['Content-Disposition'] = 'filename=order_{}.pdf"'.format(order.id)
    fs = FileSystemStorage("/tmp")
    with fs.open("cotizacion_{}.pdf") as pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'filename=cotizacion_{}.pdf'.format(cotizacion.id)
        return response

    return response
    #weasyprint.HTML(string=html).write_pdf(response,
        #stylesheets=[weasyprint.CSS(
            #settings.STATIC_ROOT + 'css/pdf.css')])
    #return response




