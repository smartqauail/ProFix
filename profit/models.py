
from django.db import models
from decimal import Decimal
from django.core.validators import MinValueValidator,MaxValueValidator
from phone_field import PhoneField
from django.utils.translation import gettext_lazy as _
from parler.models import TranslatableModel, TranslatedFields



class edificio(TranslatableModel):
    

    CHOICE=[('PFE','PFE'),
        ('PFC','PFC'),
        ('PFU','PFU'),
        ('PFH','PFH'),
        ('PFP','PFP'),
        ]

    translations = TranslatedFields(   
        
        building_code = models.CharField(_('Building Code'),max_length=3,choices=CHOICE),
        building_id = models.CharField(_('Building ID'),max_length=3),
        image = models.ImageField(_('image'),null=True, blank=True, upload_to="static/edificios/"),   
        building_name = models.CharField(_('Building name'), max_length=50,help_text='Escribir el nombre del edificio'),
        city = models.CharField(_('city'), max_length=100),
        building_levels = models.IntegerField(default=0, validators=[MaxValueValidator(99)],null=True,verbose_name=_('building_levels')),
        building_address = models.CharField(_('Building address'), max_length=250),
        building_ruc = models.PositiveIntegerField(null=True,validators=[MaxValueValidator(999999999999999)]),
        building_accountant = models.CharField(_('Building Accountant '), max_length=20),
        insurance_carrier =models.CharField(_('Building insurance carrier '), max_length=20),
        administration_manager = models.CharField(_('administration manager name'), max_length=20),
        manager_administrator_name = models.CharField(_('Manager administrator name'), max_length=50),
        administrator_email = models.EmailField(_('administrator e-mail')),
        administrator_phonenumber = PhoneField(_('administrator phonenumber'),blank=True),
        created = models.DateTimeField(auto_now_add=True,null=True),
        code= models.CharField(_('codigo'), max_length=50,blank=True)
    )
   

    class Meta:
        verbose_name = 'edificio'
        verbose_name_plural = 'edificios'

    def __str__(self):
        return 'Edificio: {}'.format(self.code)
        
    @property
    def Codigo(self):
        return ' '.join([self.building_code,' ',self.building_id,' '])


    def save(self):
        self.code = self.Codigo
        super (edificio, self).save()
       
      
       


