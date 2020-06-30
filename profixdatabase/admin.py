import csv
import datetime
from django.contrib import admin
from django.http import HttpResponse
from .models import Edificios,colegios,hospital,Particulares
from django.urls import reverse
from django.utils.safestring import mark_safe
from parler.admin import TranslatableAdmin

@admin.register(Edificios)
class EdificiosAdmin(TranslatableAdmin):
    list_display = ['code', 'building_name','administration_manager','city', 'building_ruc',
                    'manager_administrator_name','administrator_email']
    #list_filter = ['building_name', 'city', 'manager_administrator_name']

@admin.register(colegios)
class colegiosAdmin(TranslatableAdmin):
    list_display = ['code', 'building_name','administration_manager','city', 'building_ruc',
                    'manager_administrator_name','administrator_email']
    #list_filter = ['building_name', 'city', 'manager_administrator_name']

@admin.register(hospital)
class hospitalAdmin(TranslatableAdmin):
    list_display = ['code', 'building_name','administration_manager','city', 'building_ruc',
                    'manager_administrator_name','administrator_email']
    #list_filter = ['building_name', 'city', 'manager_administrator_name']

@admin.register(Particulares)
class hospitalAdmin(TranslatableAdmin):
    list_display = ['code', 'building_name','administration_manager','city', 'building_ruc',
                    'manager_administrator_name','administrator_email']
    #list_filter = ['building_name', 'city', 'manager_administrator_name']
   