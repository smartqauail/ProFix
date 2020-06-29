from django.db import models
from django.urls import reverse
from parler.models import TranslatableModel, TranslatedFields
from profixdatabase.models import Edificios


class mantenimiento(TranslatableModel):
    CHOICE=[('Correctivo','PMC'),
    ('Preventivo','PMP'),
    ('Correctivo Sistema de Emergencia','PCSE'),
    ('Correctivo Sistema de Revestimientos','PCSR'),
    ]
    translations = TranslatedFields(
        name = models.CharField(max_length=200,db_index=True,verbose_name='Tipo de Mantenimiento',choices=CHOICE),
        slug = models.SlugField(max_length=200,db_index=True,unique=True)
        )

    class Meta:
        # ordering = ('name',)
        verbose_name = 'Tipo de Mantenimiento'
        verbose_name_plural = 'Tipo de Mantenimientos'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
            return reverse('profixprojects:maintenance_list_by_category',
                           args=[self.slug])


class Project(TranslatableModel):
 
    translations = TranslatedFields(
            building_code = models.ForeignKey(Edificios,related_name='edificio',on_delete=models.CASCADE),
            name = models.CharField(max_length=200, db_index=True ,verbose_name='Nombre de Proyecto'),
            slug = models.SlugField(max_length=200, db_index=True),
            code2= models.CharField(max_length=500,blank=True,verbose_name='Codigo de Proyecto'),
            description = models.TextField(blank=True,verbose_name='Descripción de Proyecto'),
        )
    category = models.ForeignKey(mantenimiento,related_name='main',on_delete=models.CASCADE,verbose_name='Categoría de Mantenimiento')
    image = models.ImageField(upload_to='main/%Y/%m/%d',blank=True,verbose_name='Imagenes Reportadas')
    
    price = models.DecimalField(max_digits=10, decimal_places=2,verbose_name='Valor Unitario')
    available = models.BooleanField(default=True,verbose_name='Aprobado?')
    created = models.DateTimeField(auto_now_add=True,verbose_name='Fecha de creación de proyecto')
    updated = models.DateTimeField(auto_now=True,verbose_name='Fecha de última actualización de proyecto')

    class Meta:
        verbose_name = 'Proyectos para Edificios'
        verbose_name_plural = 'Proyecto para Edificio'


    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return reverse('profixprojects:Project_detail',args=[self.id, self.slug])

  
    
