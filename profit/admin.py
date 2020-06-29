from django.contrib import admin
from .models import edificio
from parler.admin import TranslatableAdmin
from django.utils.safestring import mark_safe




@admin.register(edificio)
class edificioAdmin(TranslatableAdmin):
    list_display = ['Codigo','building_name','administration_manager','manager_administrator_name','administrator_email','administrator_phonenumber',]
    readonly_fields = ["foto","code",]
    
    def foto(self, obj):
        return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
        url = obj.image.url,
        width=obj.image.width,
        height=obj.image.height,
        )
    )
