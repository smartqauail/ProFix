from django.db import models
from django.utils.translation import gettext_lazy as _
from parler.models import TranslatableModel, TranslatedFields
from profit.models import edificio
from ProMain.models import CotizacionPM
import datetime


class Registro(TranslatableModel):
    
    CHOICE=[('PRMC','PRMC'),
        ('PRMP','PRMP'),
        ('PRSE','PRSE'),
        ('PRSR','PRSR'),
        ]
    translations = TranslatedFields(
        building_code2 = models.ForeignKey(edificio,on_delete=models.CASCADE,help_text='Escribir el Codigo del edificio'),
        project_code = models.CharField(_('Project Code'),max_length=6,choices=CHOICE),
        project_id = models.CharField(_('Project ID'),max_length=3),
        project_name = models.CharField(_('Project Name'),max_length=32),
        subject = models.TextField(_('Subject')), 
        code= models.CharField(_('codigo'), max_length=50,blank=True)
        
        )
   

    class Meta:
        verbose_name = 'Registro-Edificio'
        verbose_name_plural = 'Registros-Edificios'

    def __str__(self):
        return 'Proyecto: {}'.format(self.project_name)
        
    @property
    def Codigo(self):
        return ' '.join([self.project_code,' ',self.project_id,' '])


    def save(self):
        self.code = self.Codigo
        super (Registro, self).save()

class Analitycs(models.Model):
    CHOICES=[('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
        ('5','5'),
        ('6','6'),
        ('7','7'),
        ('8','8'),
        ('9','9'),
        ('10','10'),
        ]


    projectPM = models.ForeignKey(Registro,related_name='items',on_delete=models.CASCADE)
    invoice_PM = models.ForeignKey(CotizacionPM,related_name='cotipm',on_delete=models.CASCADE)
    items = models.CharField(null=True,max_length=2,choices=CHOICES)
    price1 = models.DecimalField(_('Promain workhand Price'),max_digits=10, decimal_places=2)
    porce = models.DecimalField(_('feed Promain WorkHand'),max_digits=3, decimal_places=2)
    total2 = models.CharField(null=True,max_length=2)
   


    @property
    def Value(self):
        return self.price1 * self.porce
         
    def save(self):
        self.total2 = self.Value
        super (Analitycs2, self).save()
    

    def __str__(self):
        return '{}'.format(self.id)



    def get_cost(self):
        return self.price1 * self.porce
        
    class Meta:
        verbose_name = 'Análisis de Costo Mano de Obra'
        verbose_name_plural = 'Análisis de Costos Mano de Obra'

class Analitycs2(models.Model):
    CHOICES=[('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
        ('5','5'),
        ('6','6'),
        ('7','7'),
        ('8','8'),
        ('9','9'),
        ('10','10'),
        ]

    project = models.ForeignKey(Registro,null=True,related_name='items2',on_delete=models.CASCADE)
    invoice_PM = models.ForeignKey(CotizacionPM,null=True,related_name='cotipm2',on_delete=models.CASCADE)
    items = models.CharField(max_length=2,null=True,choices=CHOICES)
    price2 = models.DecimalField(_('ProTools Materials Price'),max_digits=10, decimal_places=2)
    porce2 = models.DecimalField(_('feed Protools Materials'),max_digits=3, decimal_places=2)
    total1 = models.CharField(null=True,max_length=2)

    @property
    def Value(self):
        return self.price2 * self.porce2
         
    def save(self):
        self.total1 = self.Value
        super (Analitycs, self).save()
    


    def __str__(self):
        return '{}'.format(self.id)



    def get_cost2(self):
        return self.price1 * self.porce2
        
    class Meta:
        verbose_name = 'Análisis de Costo Materiales'
        verbose_name_plural = 'Análisis de Costos Materiales'

class PlandeTrabajo(models.Model):
    CHOICES=[('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
        ('5','5'),
        ('6','6'),
        ('7','7'),
        ('8','8'),
        ('9','9'),
        ('10','10'),
        ]


    project2 = models.ForeignKey(Registro,null=True,related_name='items3',on_delete=models.CASCADE)
    items = models.CharField(max_length=2,null=True,choices=CHOICES)
    start_time = models.DateTimeField(null=True, blank=True)
    end_time = models.DateTimeField(null=True, blank=True)
    total = models.DateTimeField(null=True)


    @property
    def Fecha(self):
        return self.start_time - self.end_time
         
    def Value(self):
        self.total = self.Value
        super (PlandeTrabajo, self).save()


    def __str__(self):
        return '{}'.format(self.id)



    def get_cost3(self):
        return self.start_time - self.end_time
        
    class Meta:
        verbose_name = 'Plan de Trabajo'
        verbose_name_plural = 'Planes de Trabajo'



