from __future__ import unicode_literals
from django.contrib import admin
from parler.admin import TranslatableAdmin
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.utils.safestring import mark_safe
from django.db.models import F,Value,Count,Avg, Sum, Min, Max, DateTimeField
from django.db.models.functions import TruncDay,Trunc
from profixprojects.models import Project,mantenimiento

@admin.register(mantenimiento)
class mantenimientoAdmin(TranslatableAdmin):
    list_display = ['name', 'slug']

    def get_prepopulated_fields(self, request, obj=None):
            return {'slug': ('name',)}

@admin.register(Project)
class ProjectAdmin(TranslatableAdmin):
    list_display = ['code2','building_code','category','price','available','created','updated',]
    list_editable = ['available']

    def get_prepopulated_fields(self, request, obj=None):
            return {'slug': ('name',)}