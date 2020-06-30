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
from profixdatabase.models import Edificios
from profixprojects.models import Project
from coupons.models import Coupon



class Perfil(TranslatableModel):
    

    CHOICE=[('PFE','PFE'),
        ('PFC','PFC'),
        ('PFU','PFU'),
        ('PFS','PFS'),
        ('PFP','PFP'),
        ]

    translations = TranslatedFields(   
        
        building_code = models.ForeignKey(Edificios,related_name='edificios',on_delete=models.CASCADE),
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
        created = models.DateTimeField(auto_now_add=True,null=True)
    )
   

    class Meta:
        verbose_name = 'Información del Edificio'
        verbose_name_plural = 'Datos del Edificio'

    def __str__(self):
        return 'Edificio: {}'.format(self.building_code)
        
  



class Diagnostico(TranslatableModel):
    

    CHOICE=[('RMC','RMC'),
        ('RMP','RMP'),
        ('RSE','RSE'),
        ('RSR','RSR'),
        ]

    translations = TranslatedFields(   
        
        report_code = models.CharField(_('Report Code'),max_length=3,choices=CHOICE),
        report_id = models.CharField(_('Report ID'),max_length=2),
        created = models.DateTimeField(_('Date report Created'),auto_now_add=True,null=True),
        date_meet = models.DateTimeField(_('Date Technical meet'),null=True),
        project_name = models.CharField(_('Project name'), max_length=50,help_text='Escribir Nombre de Proyecto'),

        item_name = models.CharField(_('item Name'),max_length=20,null=True,blank=True),
        item_description =models.TextField(_('Item description'),null=True,blank=True),
        image_item = models.ImageField(_('image Item'),null=True, blank=True, upload_to="static/edificios/"), 

        item_name2 = models.CharField(_('item Name'),max_length=20,null=True,blank=True),
        item_description2 =models.TextField(_('Item description'),null=True,blank=True),
        image_item2 = models.ImageField(_('image Item'),null=True, blank=True, upload_to="static/edificios/"), 

        item_name3 = models.CharField(_('item Name'),max_length=20,null=True,blank=True),
        item_description3 =models.TextField(_('Item description'),null=True,blank=True),
        image_item3 = models.ImageField(_('image Item'),null=True, blank=True, upload_to="static/edificios/"), 

        promain_code = models.CharField(_('ProMain Code'),max_length=20,help_text='Codigo de Tecnico Profix Responsable'),
        dayswork = models.IntegerField(_('Calendary days'),default=0, validators=[MaxValueValidator(15)],null=True),
        code= models.CharField(_('codigo'), max_length=10,blank=True)
    )
   

    class Meta:
        verbose_name = 'Diagnostico de Mantenimiento'
        verbose_name_plural = 'Diagnostico de Mantenimiento'

    def __str__(self):
        return 'Reporte: {}'.format(self.code)
        
    @property
    def Codigo(self):
        return ' '.join([self.report_code,' ',self.report_id,' ',])


    def save(self):
        self.code = self.Codigo
        super (Diagnostico, self).save()


# Cotizaciones


class Cotizacion(models.Model):
    project_name =models.ForeignKey(Project,related_name='project',on_delete=models.CASCADE,null=True)
    report_code= models.ForeignKey(Diagnostico,related_name='project',on_delete=models.CASCADE,null=True)
    #Report_code = models.CharField(max_length=5,null=True,verbose_name='Codigo de Reporte')
    email = models.EmailField(_('e-mail'),null=True)
    address = models.CharField(_('address'), max_length=250)
    created = models.DateTimeField(auto_now_add=True,null=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)
    coupon = models.ForeignKey(Coupon,
                               related_name='projects',
                               null=True,
                               blank=True,
                               on_delete=models.SET_NULL)
    discount = models.IntegerField(default=0,
                                   validators=[MinValueValidator(0),
                                               MaxValueValidator(100)])

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return 'Cotización {}'.format(self.id)

    #def __str__(self):
        #return '{}'.format(self.first_name)

    def __str__(self):
        return self.address

    def __bool__(self):
        return self.paid

    def get_total_cost(self):
        total_cost = sum(item.get_cost() for item in self.items.all())
        return total_cost - total_cost * (self.discount / Decimal('100'))


class InvoiceItem(models.Model):
    cotizacion = models.ForeignKey(Cotizacion,
                              related_name='items',
                              on_delete=models.CASCADE)
    project = models.ForeignKey(Project,related_name='project_items',on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)



    def get_cost(self):
        return self.price * self.quantity


#Proyectos

class Proyecto(models.Model):
    project_name = models.CharField(max_length=3,null=True,verbose_name='Codigo de Proyecto')
    invoice_code = models.CharField(max_length=3,null=True,verbose_name='Codigo de Cotización')
    created = models.DateTimeField(auto_now_add=True,null=True,verbose_name='Fecha de Creación')
    Fecha = models.DateField(null=True,verbose_name='Fecha de entrega de Proyecto')
    porcet2=models.DecimalField(max_digits=5, decimal_places=2,null=True,verbose_name='Avance de Obra %')
    porcet=models.DecimalField(max_digits=5, decimal_places=2,null=True,verbose_name='Porcetanje de Anticipo %')
    value2= models.DecimalField(max_digits=10, decimal_places=2,null=True,verbose_name='Valor neto de la cotización')
    value3=models.DecimalField(max_digits=10, decimal_places=2,null=True)
    value4=models.DecimalField(max_digits=10, decimal_places=2,null=True)

    def Avance_de_Obra(self):
        if self.porcet2:
            percentage2 = round((self.porcet2), 0)
        else:
                percentage2 = 0
        return format_html(
        """
        <progress value="{0}" max="100"></progress>
            <span style="font-weight:bold">{0}%</span>
        """,
            percentage2 )

    


    @property 
    def Advance(self):
        if self.porcet and self.value2:
            advance2 =  round((self.porcet/100) * self.value2,2)
        else:
            advance2=0
        return  advance2

    @property 
    def Saldo_a_cancelar(self):
        if self.Advance and self.value2:
            saldo =  round((self.value2) - (self.Advance),2)
        else:
            saldo=0
        return  saldo
        
    

    def Anticipo(self):
        if self.value2 and self.Advance:
            percentage = round((self.Advance / self.value2*100 ), 0)
        else:
            percentage = 0
            
        return format_html(
                """
                <progress value="{0}" max="100"></progress>
                <span style="font-weight:bold">{0}%</span>
                """,
                percentage )

    

    def save(self): 
        self.value3 = self.Advance
        self.value4 = self.Saldo_a_cancelar
        super(Proyecto, self).save()

class ProyectosAvadell(Proyecto): #Extends funcs of model without creating a table in DB
    class Meta:
        proxy = True 
        verbose_name = 'Proyectos Avadell'
        verbose_name_plural = 'Proyecto Avadell'



    


