from django.db import models
from django.utils.translation import gettext_lazy as _
from parler.models import TranslatableModel, TranslatedFields
from profit.models import edificio


class CotizacionPM(TranslatableModel):
    
    CHOICE=[('PMMC','PMMC'),
        ('PMMP','PMMP'),
        ('PMSE','PMSE'),
        ('PMSR','PMSR'),
        ]
    translations = TranslatedFields(
        invoice_type = models.CharField(_('Invoice Type'),max_length=6,choices=CHOICE),
        invoice_id = models.CharField(_('Invoice ID'),max_length=3),
        project_name = models.CharField(_('Project Name'),max_length=32),
        subject = models.TextField(_('Subject')), 
        code= models.CharField(_('codigo'), max_length=50,blank=True)
        
        )
   

    class Meta:
        verbose_name = 'Cotizacion ProMain'
        verbose_name_plural = 'Cotizaciones ProMain'

    def __str__(self):
        return '{}'.format(self.Codigo)
        
    @property
    def Codigo(self):
        return ' '.join([self.invoice_type,' ',self.invoice_id,' '])


    def save(self):
        self.code = self.Codigo
        super (CotizacionPM, self).save()