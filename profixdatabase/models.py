from django.db import models
from decimal import Decimal
from django.utils.html import format_html
from django.template.defaultfilters import slugify
from django.core.validators import MinValueValidator,MaxValueValidator
from django.core.exceptions import ValidationError
from django.db.models import F,Value,Count,Avg, Sum, Min, Max, DateTimeField
from phone_field import PhoneField
from django.utils.translation import gettext_lazy as _
from parler.models import TranslatableModel, TranslatedFields



class Edificios(TranslatableModel):
    

    CHOICE=[('PFE','PFE'),
        ('PFC','PFC'),
        ('PFU','PFU'),
        ('PFS','PFS'),
        ('PFP','PFP'),
        ]

    translations = TranslatedFields(   
        
        building_code = models.CharField(_('Building Code'),max_length=3,choices=CHOICE),
        building_id = models.CharField(_('Building ID'),max_length=500),
        building_name = models.CharField(_('Building name'), max_length=50,help_text='Escribir el nombre del edificio'),
        city = models.CharField(_('city'), max_length=100),
        building_levels = models.IntegerField(default=0, validators=[MaxValueValidator(99)],null=True),
        building_address = models.CharField(_('Building address'), max_length=250),
        building_ruc = models.PositiveIntegerField(null=True,validators=[MaxValueValidator(999999999999999)]),
        building_accountant = models.CharField(_('Building Accountant '), max_length=20),
        insurance_carrier =models.CharField(_('Building insurance carrier '), max_length=20),
        administration_manager = models.CharField(_('administration manager name'), max_length=20),
        manager_administrator_name = models.CharField(_('Manager administrator name'), max_length=50),
        administrator_email = models.EmailField(_('administrator e-mail')),
        administrator_phonenumber = PhoneField(_('administrator phonenumber'),blank=True),
        created = models.DateTimeField(auto_now_add=True,null=True),
        code= models.CharField(_('codigo'), max_length=50,blank=True),
        project_number= models.CharField(_('Projects Numbers'), max_length=50,blank=True)
    )
   

    class Meta:
        verbose_name = 'Información del Edificio'
        verbose_name_plural = 'Datos del Edificio'

    def __str__(self):
        return 'Edificio: {}'.format(self.code)
        
    @property
    def Codigo(self):
        return ' '.join([self.building_code,' ',self.building_id,' '])


    def save(self):
        self.code = self.Codigo
        super (Edificios, self).save()

class colegios(TranslatableModel):
    

    CHOICE=[('PFE','PFE'),
        ('PFC','PFC'),
        ('PFU','PFU'),
        ('PFS','PFS'),
        ('PFP','PFP'),
        ]

    translations = TranslatedFields(   
        
        building_code = models.CharField(_('Building Code'),max_length=3,choices=CHOICE),
        building_id = models.CharField(_('Building ID'),max_length=500),
        building_name = models.CharField(_('Building name'), max_length=50,help_text='Escribir el nombre del edificio'),
        city = models.CharField(_('city'), max_length=100),
        buildings_levels = models.IntegerField(_('Buildings Numbers'),default=0, validators=[MaxValueValidator(99)],null=True),
        building_address = models.CharField(_('Building address'), max_length=250),
        building_ruc = models.PositiveIntegerField(null=True,validators=[MaxValueValidator(999999999999999)]),
        building_accountant = models.CharField(_('Building Accountant '), max_length=20),
        insurance_carrier =models.CharField(_('Building insurance carrier '), max_length=20),
        administration_manager = models.CharField(_('administration manager name'), max_length=20),
        manager_administrator_name = models.CharField(_('Manager administrator name'), max_length=50),
        administrator_email = models.EmailField(_('administrator e-mail')),
        administrator_phonenumber = PhoneField(_('administrator phonenumber'),blank=True),
        created = models.DateTimeField(auto_now_add=True,null=True),
        code= models.CharField(_('codigo'), max_length=50,blank=True),
        project_number= models.CharField(_('Projects Numbers'), max_length=50,blank=True)
    )
   

    class Meta:
        verbose_name = 'Instituciones Educativas'
        verbose_name_plural = 'Institución Educativa'

    def __str__(self):
        return 'Edificio: {}'.format(self.code)
        
    @property
    def Codigo(self):
        return ' '.join([self.building_code,' ',self.building_id,' '])


    def save(self):
        self.code = self.Codigo
        super (edificio, self).save()


class hospital(TranslatableModel):
    

    CHOICE=[('PFE','PFE'),
        ('PFC','PFC'),
        ('PFU','PFU'),
        ('PFS','PFS'),
        ('PFP','PFP'),
        ]

    translations = TranslatedFields(   
        
        building_code = models.CharField(_('Building Code'),max_length=3,choices=CHOICE),
        building_id = models.CharField(_('Building ID'),max_length=500),
        building_name = models.CharField(_('Building name'), max_length=50,help_text='Escribir el nombre del edificio'),
        city = models.CharField(_('city'), max_length=100),
        buildings_levels = models.IntegerField(_('Buildings Numbers'),default=0, validators=[MaxValueValidator(99)],null=True),
        building_address = models.CharField(_('Building address'), max_length=250),
        building_ruc = models.PositiveIntegerField(null=True,validators=[MaxValueValidator(999999999999999)]),
        building_accountant = models.CharField(_('Building Accountant '), max_length=20),
        insurance_carrier =models.CharField(_('Building insurance carrier '), max_length=20),
        administration_manager = models.CharField(_('administration manager name'), max_length=20),
        manager_administrator_name = models.CharField(_('Manager administrator name'), max_length=50),
        administrator_email = models.EmailField(_('administrator e-mail')),
        administrator_phonenumber = PhoneField(_('administrator phonenumber'),blank=True),
        created = models.DateTimeField(auto_now_add=True,null=True),
        code= models.CharField(_('codigo'), max_length=50,blank=True),
        project_number= models.CharField(_('Projects Numbers'), max_length=50,blank=True)
    )
   

    class Meta:
        verbose_name = 'Instituciones Sanitarias'
        verbose_name_plural = 'Institución Sanitaria'

    def __str__(self):
        return 'Edificio: {}'.format(self.code)
        
    @property
    def Codigo(self):
        return ' '.join([self.building_code,' ',self.building_id,' '])


    def save(self):
        self.code = self.Codigo
        super (edificio, self).save()

class Particulares(TranslatableModel):
    

    CHOICE=[('PFE','PFE'),
        ('PFC','PFC'),
        ('PFU','PFU'),
        ('PFS','PFS'),
        ('PFP','PFP'),
        ]

    translations = TranslatedFields(   
        
        building_code = models.CharField(_('Building Code'),max_length=3,choices=CHOICE),
        building_id = models.CharField(_('Building ID'),max_length=500),
        building_name = models.CharField(_('Building name'), max_length=50,help_text='Escribir el nombre del edificio'),
        city = models.CharField(_('city'), max_length=100),
        buildings_levels = models.IntegerField(_('Buildings Numbers'),default=0, validators=[MaxValueValidator(99)],null=True),
        building_address = models.CharField(_('Building address'), max_length=250),
        building_ruc = models.PositiveIntegerField(null=True,validators=[MaxValueValidator(999999999999999)]),
        building_accountant = models.CharField(_('Building Accountant '), max_length=20),
        insurance_carrier =models.CharField(_('Building insurance carrier '), max_length=20),
        administration_manager = models.CharField(_('administration manager name'), max_length=20),
        manager_administrator_name = models.CharField(_('Manager administrator name'), max_length=50),
        administrator_email = models.EmailField(_('administrator e-mail')),
        administrator_phonenumber = PhoneField(_('administrator phonenumber'),blank=True),
        created = models.DateTimeField(auto_now_add=True,null=True),
        code= models.CharField(_('codigo'), max_length=50,blank=True),
        project_number= models.CharField(_('Projects Numbers'), max_length=50,blank=True)
    )
   

    class Meta:
        verbose_name = 'Instituciones Particulares'
        verbose_name_plural = 'Institución Particular'

    def __str__(self):
        return 'Edificio: {}'.format(self.code)
        
    @property
    def Codigo(self):
        return ' '.join([self.building_code,' ',self.building_id,' '])


    def save(self):
        self.code = self.Codigo
        super (edificio, self).save()