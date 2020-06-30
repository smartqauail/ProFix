from __future__ import unicode_literals
from django.contrib import admin
from .models import Perfil,Diagnostico,Proyecto,ProyectosAvadell,Cotizacion,InvoiceItem
from parler.admin import TranslatableAdmin
from django.urls import reverse
from django.http import HttpResponse
from django.utils.translation import gettext_lazy as _
from django.utils.safestring import mark_safe
from django.db.models import F,Value,Count,Avg, Sum, Min, Max, DateTimeField
from django.db.models.functions import TruncDay,Trunc



def get_next_in_date_hierarchy(request, date_hierarchy):
    
    if date_hierarchy + '__day' in request.GET:
        return 'hour'
    if date_hierarchy + '__month' in request.GET:
        return 'day'
    if date_hierarchy + '__year' in request.GET:
        return 'week'
    return 'month'




def reportp_detail(obj):
    return mark_safe('<a href="{}">Cotización</a>'.format(
        reverse('Avadell:admin_cotizacion_detail', args=[obj.id])))

class InvoiceItemInline(admin.TabularInline):
    model = InvoiceItem
    raw_id_fields = ['project']

def reportp_pdf(obj):
    return mark_safe('<a href="{}">Cotización-PDF</a>'.format(
        reverse('Avadell:admin_cotizacion_pdf', args=[obj.id])))
    reportp_pdf.short_description = 'cotizacion'

@admin.register(Cotizacion)
class CotizacionAdmin(admin.ModelAdmin):
    list_display = ['id', 'project_name', 'report_code', 'email','created', 'updated', reportp_pdf, reportp_detail]
    list_filter = ['project_name', 'created', 'updated']
    inlines = [InvoiceItemInline]



    

@admin.register(Perfil)
class PerfilAdmin(TranslatableAdmin):
    list_display = ['building_code','building_name','administration_manager','manager_administrator_name','administrator_email','administrator_phonenumber',]
    readonly_fields = ["foto",]
    
    def foto(self, obj):
        return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
        url = obj.image.url,
        width=obj.image.width,
        height=obj.image.height,
        )
    )
@admin.register(Diagnostico)
class DiagnosticoAdmin(TranslatableAdmin):
    list_display = ['Codigo','project_name','created','date_meet','dayswork',]
    readonly_fields = ["code",]





@admin.register(Proyecto)
class ProyectoAdmin(admin.ModelAdmin):
    list_display = ['project_name','Advance','Anticipo','Avance_de_Obra','Fecha']
    readonly_fields = ["value3","value4"]

@admin.register(ProyectosAvadell)
class ProyectosAvadelldmin(admin.ModelAdmin):
    change_list_template = 'admin/order_summary_change_list.html'
    date_hierarchy = 'created'
    # Prevenimos que se adicionen valores a la paginacion.
    show_full_result_count = True
    actions = None
    
    def has_add_permission(self, request):
        return False
    def has_delete_permission(self, request, obj=None):
        return False
        
    def has_change_permission(self, request, obj=None):
        return True
        
    def has_module_permission(self, request):
        return True
        
        
        
    def changelist_view(self, request, extra_context=None):
        response = super().changelist_view(request,extra_context=extra_context,)
        try:
            qs = response.context_data['cl'].queryset
        except (AttributeError, KeyError):
            return response
            
        metrics = {
            'total': Count('id'),
            'date': Count('Fecha'),
            'valor_cotizado':Sum('value2'),
            'valor_pagado':Sum('value3'),
            'valor_a_pagar': Sum(F('value2')-F('value3')),
            'Porcentaje_Pagado': Sum(((F('value3')/F('value2'))*100)),
            'avance_de_obra':Sum(F('porcet2')),
            'porcetotal': Sum(((F('value2')/F('value3'))*100)),
            }
        response.context_data['summary'] = list(qs.values('id','value2','value3','value4','project_name','porcet2','created','Fecha',)
        .annotate(**metrics)
        .order_by('-created')
        )
        response.context_data['summary_total'] = dict(qs.aggregate(**metrics))
        period = get_next_in_date_hierarchy(request, self.date_hierarchy)
        response.context_data['period'] = period
        summary_over_time = qs.annotate(period=Trunc('created', period, output_field=DateTimeField()),).values('period').annotate(total=Sum(F('value2'))).order_by('period')
        summary_range = summary_over_time.aggregate(low=Min(('total')),high=Max(('total')),)
        high = summary_range.get('high', 0)
        low = summary_range.get('low', 0)
        
        response.context_data['summary_over_time'] = [{
        'period': x['period'],
        'total': x[('total')] or 0,
        'pct': 
            round(((((x[('total')] or 0) - low) / (high - low) )* 100),-1)
            if high > low else 0,
        } for x in summary_over_time]
        return response









    