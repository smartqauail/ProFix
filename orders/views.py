from django.urls import reverse
from django.shortcuts import render, redirect
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart
from .tasks import order_created
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import get_object_or_404
from .models import Order,OrderItem
from shop.models import Product,Category
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



def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)

        if form.is_valid():
            order = form.save(commit=False)
            if cart.coupon:
                order.coupon = cart.coupon
                order.discount = cart.coupon.discount
            order.save()

            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            # clear the cart
            cart.clear()
            # launch asynchronous task
            order_created.delay(order.id)
            # set the order in the session
            request.session['order_id'] = order.id
    
            # redirect for payment
            return redirect(reverse('payment:process'))
    else:
        form = OrderCreateForm()
    return render(request,
                  'orders/order/create.html',
                  {'cart': cart, 'form': form})


@staff_member_required
def admin_order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request,
                  'admin/orders/order/detail.html',
                  {'order': order})


@staff_member_required
def admin_order_pdf(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    #paid = get_object_or_404(Order, paid=order.paid)
    #name  = get_object_or_404(Order, first_name=order.first_name)
    #address  = get_object_or_404(Order, address=order.address)

    html = render_to_string('orders/order/pdf.html',
                            {'order': order})
                            
    doc = SimpleInvoice("/tmp/order_{}.pdf")
   
    
    doc.is_paid = order.paid # Paid stamp, optional
    doc.invoice_info = InvoiceInfo(order.id, order.created , order.updated)  # Invoice info, optional
    
    # Service Provider Info, optional
    doc.service_provider_info = ServiceProviderInfo(
    name= order.first_name, 
    street = order.address,
    city= order.city,
    post_code='222222',
    state= order.postal_code,
    country='My Country',
    vat_tax_number='Vat/Tax number',
    email=order.email
   
    )
   

# Client info, optional
    doc.client_info = ClientInfo(
    email='client@example.com',
    name= order.project_name,
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
    with fs.open("order_{}.pdf") as pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'filename=order_{}.pdf'.format(order.id)
        return response

    return response
    #weasyprint.HTML(string=html).write_pdf(response,
        #stylesheets=[weasyprint.CSS(
            #settings.STATIC_ROOT + 'css/pdf.css')])
    #return response




