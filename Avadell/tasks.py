from celery import task
from django.core.mail import send_mail
from Avadell.models import Cotizacion,Perfil

@task
def invoice_created(cotizacion_id):
    """
    Task to send an e-mail notification when an order is 
    successfully created.
    """
    cotizacion = cotizacion.objects.get(id=cotizacion_id)
    subject = 'Cotización nr. {}'.format(cotizacion.id)
    message = 'Querido {},\n\nYou have successfully placed an order.\
                  Your order id is {}.'.format(Perfil.manager_administrator_name,
                                            cotizacion.id)
    mail_sent = send_mail(subject,
                          message,
                          'admin@myshop.com',
                          [cotizacion.email])
    return mail_sent
