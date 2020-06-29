from django.urls import path
from . import views
from django.utils.translation import gettext_lazy as _


app_name = 'Avadell'

urlpatterns = [
    path('create/', views.invoice_created, name='invoice_create'),
    path('admin/cotizacion/<int:cotizacion_id>/', views.admin_cotizacion_detail, name='admin_cotizacion_detail'),
    path('admin/cotizacion/<int:cotizacion_id>/pdf/', views.admin_cotizacion_pdf, name='admin_cotizacion_pdf'),
]
