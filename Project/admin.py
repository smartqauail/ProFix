from django.contrib import admin
from .models import Registro,Analitycs,Analitycs2,PlandeTrabajo
from profit.models import edificio
from parler.admin import TranslatableAdmin
from django.utils.safestring import mark_safe


class AnalitycsItemInline(admin.TabularInline):
    readonly_fields = ["total2",]
    model = Analitycs

class Analitycs2ItemInline(admin.TabularInline):
    readonly_fields = ["total1",]
    model = Analitycs2
class PlandeTrabajoItemInline(admin.TabularInline):
    readonly_fields = ["total",]
    model = PlandeTrabajo
   




@admin.register(Registro)
class RegistroAdmin(TranslatableAdmin):
    list_display = ['Codigo','project_name','building_code2',]
    readonly_fields = ["code",]
    search_fields=('project_name',)
    inlines = [AnalitycsItemInline,Analitycs2ItemInline,PlandeTrabajoItemInline]
    





  
   
   
  