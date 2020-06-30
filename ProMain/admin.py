from django.contrib import admin
from profit.models import edificio
from ProMain.models import CotizacionPM
from parler.admin import TranslatableAdmin
from django.utils.safestring import mark_safe

@admin.register(CotizacionPM)
class CotizacionPMAdmin(TranslatableAdmin):
    list_display = ['project_name',]