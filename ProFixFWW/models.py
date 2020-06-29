from django.db import models
from django.shortcuts import render
from wagtail.core.models import Page,Orderable
from modelcluster.fields import ParentalKey
from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.contrib.forms.edit_handlers import FormSubmissionsPanel
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import (
    FieldPanel, FieldRowPanel,
    InlinePanel, MultiFieldPanel, 
)
from wagtail.search import index



# pagina de inicio
class consultas(AbstractFormField):
    page = ParentalKey('index', on_delete=models.CASCADE, related_name='form_fields')

class Index(AbstractEmailForm):
    # Empieza Barner de Inicio
    intro = RichTextField(blank=True,verbose_name='Titulo del Barner')
    intro2 = RichTextField(blank=True,verbose_name='Subtitulo del Barner ')
    # Empieza Barner de servicios
    BS = RichTextField(blank=True,verbose_name='info del Barner-servicios ')
    BSSE = RichTextField(blank=True,verbose_name='info del Barner-SSE')
    BSRP = RichTextField(blank=True,verbose_name='info del Barner-SRP')
    BSMC = RichTextField(blank=True,verbose_name='info del Barner-SMC')
    BSMP = RichTextField(blank=True,verbose_name='info del Barner-SMP')
    # Empieza Barner de estamos trabajando
    barnert= models.CharField(max_length=150, null=True, blank=True,verbose_name='Descripcion de los trabajos en ejecucion ')
    apro = models.CharField(max_length=150, null=True, blank=True,verbose_name='Esta aprobado?')
    name2 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Direccion del edificio')
    name3 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Direccion del edificio-2')
    name4 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Direccion del edificio-3')
    name5 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Direccion del edificio-4')
    name6 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Direccion del edificio-5')
    name7 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Direccion del edificio-6')
    promo = models.CharField(max_length=150, null=True, blank=True,verbose_name='Escriba promoción, si lo esta-obra-1')
    city = models.CharField(max_length=150, null=True, blank=True,verbose_name='ciudad donde se ejecuto la obra-1')
    promo2 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Escriba promoción, si lo esta-obra-2')
    city2 = models.CharField(max_length=150, null=True, blank=True,verbose_name='ciudad donde se ejecuto la obra2')
    promo3 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Escriba promoción, si lo esta-obra-3')
    city3 = models.CharField(max_length=150, null=True, blank=True,verbose_name='ciudad donde se ejecuto la obra-3')
    promo4 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Escriba promoción, si lo esta-obra-4')
    city4 = models.CharField(max_length=150, null=True, blank=True,verbose_name='ciudad donde se ejecuto la -obra-4')
    promo5 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Escriba promoción, si lo esta-obra-5')
    city5 = models.CharField(max_length=150, null=True, blank=True,verbose_name='ciudad donde se ejecuto la obra-5')
    promo6 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Escriba promoción, si lo esta-obra-6')
    city6 = models.CharField(max_length=150, null=True, blank=True,verbose_name='ciudad donde se ejecuto la obra-6')
    # Emipieza Barner De buscar empleo
    info= models.CharField(max_length=150, null=True, blank=True,verbose_name='Informacion general para encontrar empleo')
     # informacion Barner De buscar empleo
    info2= RichTextField(blank=True,verbose_name='infomacion ProFix-Group-parrafo1')
    info3= RichTextField(blank=True,verbose_name='infomacion ProFix-Group-parrafo2')
    info4= RichTextField(blank=True,verbose_name='infomacion ProFix-Group-parrafo3')
    # Emipieza Como trabajamos
    info5= RichTextField(blank=True,verbose_name='Descripcion corta de ProFix-systems')
    info6= RichTextField(blank=True,verbose_name='Descripcion corta de ProMain')
    info7= RichTextField(blank=True,verbose_name='Descripcion corta de ProTools')
    info8= RichTextField(blank=True,verbose_name='Descripcion corta de ProFits')
     # Emipieza BArner de promociones
    publi= models.CharField(max_length=150, null=True, blank=True,verbose_name='Decir en que servicio hay promocion')
    info9= RichTextField(blank=True,verbose_name='Descripcion corta de la promocion')
    # Barner de ProFix-crew
    info10= RichTextField(blank=True,verbose_name='Titulo del barner-Crew')
    info11= models.CharField(max_length=150, null=True, blank=True,verbose_name='descripcion Crew')
    etiproc= models.CharField(max_length=150,null=True, blank=True,verbose_name='Proyectos Finalizados')

    presidente ='P'
    gerente = 'G'
    administrador='A'
    tecnico = 'T'
    administrador2='A1'

    categoria =[(presidente,'Presidente'),
    (gerente,'C.O'),
    (administrador,'Departamento de Comercializacion'),
    (tecnico,'Departamento técnico'),
    (administrador2,'Departamento de Desarollo')
    ]   
    crewname=models.CharField(max_length=150, null=True, blank=True,verbose_name='Nombre del crew1')
    info12 = models.CharField(choices=categoria,max_length=150, null=True, blank=True,verbose_name='Departamento al que pertenece-crew1')
    acticrew= models.CharField(max_length=150, null=True, blank=True,verbose_name='actividad del crew1')
    proc= models.IntegerField(null=True, blank=True,verbose_name='Numero de Proyectos Ejecutados-crew1')

    crewname2=models.CharField(max_length=150, null=True, blank=True,verbose_name='Nombre del crew2')
    info13 = models.CharField(choices=categoria,max_length=150, null=True, blank=True,verbose_name='Departamento al que pertenece-crew2')
    acticrew2= models.CharField(max_length=150, null=True, blank=True,verbose_name='actividad del crew2')
    proc2= models.IntegerField(null=True, blank=True,verbose_name='Numero de Proyectos Ejecutados-crew2')

    crewname3=models.CharField(max_length=150, null=True, blank=True,verbose_name='Nombre del crew3')
    info14 = models.CharField(choices=categoria,max_length=150, null=True, blank=True,verbose_name='Departamento al que pertenece-crew3')
    acticrew3= models.CharField(max_length=150, null=True, blank=True,verbose_name='actividad del crew3')
    proc3= models.IntegerField(null=True, blank=True,verbose_name='Numero de Proyectos Ejecutados-crew3')

    crewname4=models.CharField(max_length=150, null=True, blank=True,verbose_name='Nombre del crew4')
    info15 = models.CharField(choices=categoria,max_length=150, null=True, blank=True,verbose_name='Departamento al que pertenece-crew4')
    acticrew4= models.CharField(max_length=150, null=True, blank=True,verbose_name='actividad del crew4')
    proc4= models.IntegerField(null=True, blank=True,verbose_name='Numero de Proyectos Ejecutados-crew4')

    #Barner Aliados
    aliadname=models.CharField(max_length=150, null=True, blank=True,verbose_name='Nombre empresa aliado-1')
    aliadifo=models.CharField(max_length=150, null=True, blank=True,verbose_name='concepto empresa aliado-1')
    aliadref= RichTextField(blank=True,verbose_name='Comentario del Aliado-1 a Profix')

    aliadname2=models.CharField(max_length=150, null=True, blank=True,verbose_name='Nombre empresa aliado-1')
    aliadifo2=models.CharField(max_length=150, null=True, blank=True,verbose_name='concepto empresa aliado-1')
    aliadref2= RichTextField(blank=True,verbose_name='Comentario del Aliado-1 a Profix')

    aliadname3=models.CharField(max_length=150, null=True, blank=True,verbose_name='Nombre empresa aliado-1')
    aliadifo3=models.CharField(max_length=150, null=True, blank=True,verbose_name='concepto empresa aliado-1')
    aliadref3= RichTextField(blank=True,verbose_name='Comentario del Aliado-1 a Profix')

    aliadname4=models.CharField(max_length=150, null=True, blank=True,verbose_name='Nombre empresa aliado-1')
    aliadifo4=models.CharField(max_length=150, null=True, blank=True,verbose_name='concepto empresa aliado-1')
    aliadref4= RichTextField(blank=True,verbose_name='Comentario del Aliado-1 a Profix')

    aliadname5=models.CharField(max_length=150, null=True, blank=True,verbose_name='Nombre empresa aliado-1')
    aliadifo5=models.CharField(max_length=150, null=True, blank=True,verbose_name='concepto empresa aliado-1')
    aliadref5= RichTextField(blank=True,verbose_name='Comentario del Aliado-1 a Profix')

    consulta= RichTextField(blank=True,verbose_name='Mensaje para que nos consulten por el formulario')
    thank_you_text = RichTextField(blank=True)
    # galeria de imagenes barner de presentacion
    
    content_panels = AbstractEmailForm.content_panels + Page.content_panels + [

        FieldPanel('intro', classname="full"),
        FieldPanel('intro2', classname="full"),
        FieldPanel('BS', classname="full"),
        FieldPanel('BSSE', classname="full"),
        FieldPanel('BSRP', classname="full"),
        FieldPanel('BSMC', classname="full"),
        FieldPanel('BSMP', classname="full"),
        FieldPanel('apro', classname="full"),
        FieldPanel('name2', classname="full"),
        FieldPanel('name3', classname="full"),
        FieldPanel('name4', classname="full"),
        FieldPanel('name5', classname="full"),
        FieldPanel('name6', classname="full"),
        FieldPanel('name7', classname="full"),
        FieldPanel('promo', classname="full"),
        FieldPanel('city', classname="full"),
        FieldPanel('promo2', classname="full"),
        FieldPanel('city2', classname="full"),
        FieldPanel('promo3', classname="full"),
        FieldPanel('city3', classname="full"),
        FieldPanel('promo4', classname="full"),
        FieldPanel('city4', classname="full"),
        FieldPanel('promo5', classname="full"),
        FieldPanel('city5', classname="full"),
        FieldPanel('promo6', classname="full"),
        FieldPanel('city6', classname="full"),
        FieldPanel('info', classname="full"),
        FieldPanel('info2', classname="full"),
        FieldPanel('info3', classname="full"),
        FieldPanel('info4', classname="full"),
        FieldPanel('info5', classname="full"),
        FieldPanel('info6', classname="full"),
        FieldPanel('info7', classname="full"),
        FieldPanel('info8', classname="full"),
        FieldPanel('info9', classname="full"),
        FieldPanel('publi', classname="full"),
        FieldPanel('info10', classname="full"),
        FieldPanel('info11', classname="full"),
        FieldPanel('info12', classname="full"),
        FieldPanel('info13', classname="full"),
        FieldPanel('info14', classname="full"),
        FieldPanel('info15', classname="full"),
        FieldPanel('crewname', classname="full"),
        FieldPanel('crewname2', classname="full"),
        FieldPanel('crewname3', classname="full"),
        FieldPanel('crewname4', classname="full"),
        FieldPanel('acticrew', classname="full"),
        FieldPanel('acticrew2', classname="full"),
        FieldPanel('acticrew3', classname="full"),
        FieldPanel('acticrew4', classname="full"),
        FieldPanel('proc', classname="full"),
        FieldPanel('proc2', classname="full"),
        FieldPanel('proc3', classname="full"),
        FieldPanel('proc4', classname="full"),
        FieldPanel('etiproc', classname="full"),
        FieldPanel('aliadname', classname="full"),
        FieldPanel('aliadifo', classname="full"),
        FieldPanel('aliadref', classname="full"),
        FieldPanel('aliadname2', classname="full"),
        FieldPanel('aliadifo2', classname="full"),
        FieldPanel('aliadref2', classname="full"),
        FieldPanel('aliadname3', classname="full"),
        FieldPanel('aliadifo3', classname="full"),
        FieldPanel('aliadref3', classname="full"),
        FieldPanel('aliadname4', classname="full"),
        FieldPanel('aliadifo4', classname="full"),
        FieldPanel('aliadref4', classname="full"),
        FieldPanel('aliadname5', classname="full"),
        FieldPanel('aliadifo5', classname="full"),
        FieldPanel('aliadref5', classname="full"),
        FieldPanel('consulta', classname="full"),

        InlinePanel('galleria', label="Imagen de Fondo Barner"),
        FormSubmissionsPanel(),
        InlinePanel('form_fields', label="consultas"),
        FieldPanel('thank_you_text', classname="full"),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('from_address', classname="col6"),
                FieldPanel('to_address', classname="col6"),
            ]),
            FieldPanel('subject'),
        ], "Email"),
        
         ]
        
class GaleriadeImagenes(Orderable):
    page = ParentalKey(Index, on_delete=models.CASCADE, related_name='galleria')
    image = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Imagen de Fondo del Barner')
    # galeria de imagenes barner de servicios
    image2 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Imagen de Fondo del Barner-servicios')
    # galeria de imagenes barner de Estamos trabajando
    image3 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Imagen de trabajos-profix-1')
    image4 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Imagen de trabajos-profix-2')
    image5 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Imagen de trabajos-profix-3')
    image6 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Imagen de trabajos-profix-4')
    image7 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Imagen de trabajos-profix-5')
    # Fondo Barner buscando trabajo
    image8 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Imagen de Fondo barner de Buscar trabajo')
    # Logotipo de barner info ProFixGroup
    logo = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Logotipo de ProFix-Group')
    image9 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Imagen de Fondo del Barner publicitario')
    
    # Fotos de perfil ProFixCreW
    crew= models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto de perfil-ProFix Crew1')
    crew2= models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto de perfil-ProFix Crew2')
    crew3= models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto de perfil-ProFix Crew3')
    crew4= models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto de perfil-ProFix Crew4')
     # Logos empresas aliadas
    logo2= models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Logotipo empresa aliada-1')
    logo3= models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Logotipo empresa aliada-2')
    logo4= models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Logotipo empresa aliada-3')
    logo5= models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Logotipo empresa aliada-4')
    logo6= models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Logotipo empresa aliada-5')
    logo7 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Logo Smart Quail')
    logo8 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Logo de ProFix en barra de navegacion')
    logo9 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Logo de ProFix blanco en pie de pagina')

    panels = [
        ImageChooserPanel('image'),
        ImageChooserPanel('image2'),
        ImageChooserPanel('image3'),
        ImageChooserPanel('image4'),
        ImageChooserPanel('image5'),
        ImageChooserPanel('image6'),
        ImageChooserPanel('image7'),
        ImageChooserPanel('image8'),
        ImageChooserPanel('image9'),
        ImageChooserPanel('logo'),
        ImageChooserPanel('crew'),
        ImageChooserPanel('crew2'),
        ImageChooserPanel('crew3'),
        ImageChooserPanel('crew4'),
        ImageChooserPanel('logo2'),
        ImageChooserPanel('logo3'),
        ImageChooserPanel('logo4'),
        ImageChooserPanel('logo5'),
        ImageChooserPanel('logo6'),
        ImageChooserPanel('logo7'),
        ImageChooserPanel('logo8'),
        ImageChooserPanel('logo9'),
    ]
    
class FormField(AbstractFormField):
    page = ParentalKey('index_servicios_emergencia', on_delete=models.CASCADE, related_name='form_fields')

class index_servicios_emergencia(AbstractEmailForm):
    
    siren='siren'
    roller='roller'
    lista='list'
    tool='toolbox'

    categorias=[(siren,'siren'),
    (roller,'roller'),
    (lista,'list'),(tool,'toolbox'),
    ]

    primary='primary'
    secundary ='secundary'
    colors=[(primary,'primary'),(secundary ,'secundary')]

    black='Black'
    promocion='Oferta'
    ofert=[(black,'Black'),(promocion,'Oferta')]

    intro = RichTextField(blank=True,verbose_name='Titulo del Barner')
    sub_intro = RichTextField(blank=True,verbose_name='Informacion general')

    introe = RichTextField(blank=True,verbose_name='Titulo del paquete de servicios Emergencia')
    sub_introe = RichTextField(blank=True,verbose_name='Informacion general paquete de servicios Emergencia')
    introseg = RichTextField(blank=True,verbose_name='Titulo del paquete de servicios seguridad')
    sub_introseg = RichTextField(blank=True,verbose_name='Informacion general paquete de servicios seguridad')

    back = models.CharField(max_length=150, null=True, blank=True,verbose_name='En que paginas estas?')
    icon= models.CharField(choices=categorias,max_length=150, null=True, blank=True,verbose_name='Elije el icono')

    items = models.CharField(max_length=150, null=True, blank=True,verbose_name='Plan Basico de emergencia')
    item2 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Plan interiores de emergencia')
    item3 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Plan Exteriores de emergencia')
    item4 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Plan autoproteccion de emergencia')
    item5 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Suministros de emergencia')
    item6 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Contruccion de emergencia')
    item7 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Vigilancia ')
    item8 = models.CharField(max_length=150, null=True, blank=True,verbose_name='accesos')

    certi = models.CharField(max_length=150, null=True, blank=True,verbose_name='Certificado por:')
    city = models.CharField(max_length=150, null=True, blank=True,verbose_name='Ciudad')
    term = RichTextField(blank=True,verbose_name='Informacion legal del servicio')

    promo= models.CharField(choices=colors,max_length=150, null=True, blank=True,verbose_name='Elije el color promocional')
    oferta= models.CharField(choices=ofert,max_length=150, null=True, blank=True,verbose_name='Elije el color promocional')
    promo2= models.CharField(choices=colors,max_length=150, null=True, blank=True,verbose_name='Elije el color promocional')
    oferta2= models.CharField(choices=ofert,max_length=150, null=True, blank=True,verbose_name='Elije el color promocional')
    promo3= models.CharField(choices=colors,max_length=150, null=True, blank=True,verbose_name='Elije el color promocional')
    oferta3= models.CharField(choices=ofert,max_length=150, null=True, blank=True,verbose_name='Elije el color promocional')
    promo4= models.CharField(choices=colors,max_length=150, null=True, blank=True,verbose_name='Elije el color promocional')
    oferta4= models.CharField(choices=ofert,max_length=150, null=True, blank=True,verbose_name='Elije el color promocional')
    promo5= models.CharField(choices=colors,max_length=150, null=True, blank=True,verbose_name='Elije el color promocional')
    oferta5= models.CharField(choices=ofert,max_length=150, null=True, blank=True,verbose_name='Elije el color promocional')
    promo6= models.CharField(choices=colors,max_length=150, null=True, blank=True,verbose_name='Elije el color promocional')
    oferta6= models.CharField(choices=ofert,max_length=150, null=True, blank=True,verbose_name='Elije el color promocional')
    promo7= models.CharField(choices=colors,max_length=150, null=True, blank=True,verbose_name='Elije el color promocional')
    oferta7= models.CharField(choices=ofert,max_length=150, null=True, blank=True,verbose_name='Elije el color promocional')
    promo8= models.CharField(choices=colors,max_length=150, null=True, blank=True,verbose_name='Elije el color promocional')
    oferta8= models.CharField(choices=ofert,max_length=150, null=True, blank=True,verbose_name='Elije el color promocional')

    image = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Imagen de Fondo del Barner-servicios')
    confirmacion = models.CharField( max_length=255,blank=True,null=True ,help_text="El texto de que efectivamente la cotizacion llega pronto")
    thank_you_text = RichTextField(blank=True)
   


    content_panels = AbstractEmailForm.content_panels + Page.content_panels + [
        FieldPanel('intro', classname="full"),
        FieldPanel('sub_intro', classname="full"),
        FieldPanel('icon', classname="full"),
        FieldPanel('items', classname="full"),
        FieldPanel('promo', classname="full"),
        FieldPanel('oferta', classname="full"),

        FieldPanel('introe', classname="full"),
        FieldPanel('sub_introe', classname="full"),

        FieldPanel('item2', classname="full"),
        FieldPanel('promo2', classname="full"),
        FieldPanel('oferta2', classname="full"),

        FieldPanel('item3', classname="full"),
        FieldPanel('promo3', classname="full"),
        FieldPanel('oferta3', classname="full"),

        FieldPanel('item4', classname="full"),
        FieldPanel('promo4', classname="full"),
        FieldPanel('oferta4', classname="full"),

        FieldPanel('item5', classname="full"),
        FieldPanel('promo5', classname="full"),
        FieldPanel('oferta5', classname="full"),

        FieldPanel('item6', classname="full"),
        FieldPanel('promo6', classname="full"),
        FieldPanel('oferta6', classname="full"),

        FieldPanel('introseg', classname="full"),
        FieldPanel('sub_introseg', classname="full"),

        FieldPanel('item7', classname="full"),
        FieldPanel('promo7', classname="full"),
        FieldPanel('oferta7', classname="full"),

         FieldPanel('item8', classname="full"),
        FieldPanel('promo8', classname="full"),
        FieldPanel('oferta8', classname="full"),

        

        FieldPanel('certi', classname="full"),
        FieldPanel('city', classname="full"),
        FieldPanel('term', classname="full"),
        FieldPanel('back', classname="full"),

        InlinePanel('galleria2', label="Imagen de servicios"),
        FieldPanel('confirmacion'),

        FormSubmissionsPanel(),
        InlinePanel('form_fields', label="Form fields"),
        FieldPanel('thank_you_text', classname="full"),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('from_address', classname="col6"),
                FieldPanel('to_address', classname="col6"),
            ]),
            FieldPanel('subject'),
        ], "Email"),
    ]

class Banco_de_imagenes_servicios_emergencia(Orderable):
    pageS = ParentalKey(index_servicios_emergencia, on_delete=models.CASCADE, related_name='galleria2')

    image = models.ForeignKey('wagtailimages.Image', on_delete=models.CASCADE, related_name='+',verbose_name='Imagen Barner',null=True)
    image2 = models.ForeignKey('wagtailimages.Image', on_delete=models.CASCADE, related_name='+',verbose_name='Imagen-plan de emergencia B',null=True)
    image3 = models.ForeignKey('wagtailimages.Image', on_delete=models.CASCADE, related_name='+',verbose_name='Imagen-plan de emergencia I',null=True)
    image4 = models.ForeignKey('wagtailimages.Image', on_delete=models.CASCADE, related_name='+',verbose_name='Imagen-plan de emergencia E',null=True)
    image5 = models.ForeignKey('wagtailimages.Image', on_delete=models.CASCADE, related_name='+',verbose_name='Imagen-plan de emergencia A',null=True)
    image6 = models.ForeignKey('wagtailimages.Image', on_delete=models.CASCADE, related_name='+',verbose_name='Imagen-plan de emergencia Suministros',null=True)
    image7 = models.ForeignKey('wagtailimages.Image', on_delete=models.CASCADE, related_name='+',verbose_name='Imagen-plan de emergencia Construccion',null=True)
    image8 = models.ForeignKey('wagtailimages.Image', on_delete=models.CASCADE, related_name='+',verbose_name='Imagen-plan de emergencia vigilancia',null=True)
    image9 = models.ForeignKey('wagtailimages.Image', on_delete=models.CASCADE, related_name='+',verbose_name='Imagen-plan de emergencia accesos',null=True)
   
    image_2 = models.ForeignKey('wagtailimages.Image', on_delete=models.CASCADE, related_name='+',verbose_name='Imagen-info plan de emergencia B',null=True)
    image_3 = models.ForeignKey('wagtailimages.Image', on_delete=models.CASCADE, related_name='+',verbose_name='Imagen-info plan de emergencia I',null=True)
    image_4 = models.ForeignKey('wagtailimages.Image', on_delete=models.CASCADE, related_name='+',verbose_name='Imagen-info plan de emergencia E',null=True)
    image_5 = models.ForeignKey('wagtailimages.Image', on_delete=models.CASCADE, related_name='+',verbose_name='Imagen-info plan de emergencia A',null=True)
    image_6 = models.ForeignKey('wagtailimages.Image', on_delete=models.CASCADE, related_name='+',verbose_name='Imagen-info plan de emergencia Suministros',null=True)
    image_7 = models.ForeignKey('wagtailimages.Image', on_delete=models.CASCADE, related_name='+',verbose_name='Imagen-info plan de emergencia Construccion',null=True)
    image_8 = models.ForeignKey('wagtailimages.Image', on_delete=models.CASCADE, related_name='+',verbose_name='Imagen-info plan de emergencia vigilancia',null=True)
    image_9 = models.ForeignKey('wagtailimages.Image', on_delete=models.CASCADE, related_name='+',verbose_name='Imagen-info plan de emergencia accesos',null=True)
    
    panels = [
        ImageChooserPanel('image'),
        ImageChooserPanel('image2'),
        ImageChooserPanel('image_2'),
        ImageChooserPanel('image3'),
        ImageChooserPanel('image_3'),
        ImageChooserPanel('image4'),
        ImageChooserPanel('image_4'),
        ImageChooserPanel('image5'),
        ImageChooserPanel('image_5'),
        ImageChooserPanel('image6'),
        ImageChooserPanel('image_6'),
        ImageChooserPanel('image7'),
        ImageChooserPanel('image_7'),
        ImageChooserPanel('image8'),
        ImageChooserPanel('image_8'),
        ImageChooserPanel('image9'),        
        ImageChooserPanel('image_9'),
    ]

# Pagina de presentacion Servicios---------------------------------------->
   


#Pagina de servicios de Mantenimiento

class FormField2(AbstractFormField):
    page = ParentalKey('index_servicios_mantenimiento', on_delete=models.CASCADE, related_name='form_fields')

class index_servicios_mantenimiento(AbstractEmailForm):
    
    siren='siren'
    roller='roller'
    lista='list'
    tool='toolbox'

    categorias=[(siren,'siren'),
    (roller,'roller'),
    (lista,'list'),(tool,'toolbox'),
    ]

    primary='primary'
    secundary ='secundary'
    colors=[(primary,'primary'),(secundary ,'secundary')]

    black='Black'
    promocion='Oferta'
    ofert=[(black,'Black'),(promocion,'Oferta')]

    intro = RichTextField(blank=True,verbose_name='Titulo del Barner')
    sub_intro = RichTextField(blank=True,verbose_name='Informacion general')

    introp = RichTextField(blank=True,verbose_name='Titulo del Pauqete Promocional')
    sub_introp = RichTextField(blank=True,verbose_name='Informacion general Pauqete Promocional')

    intros = RichTextField(blank=True,verbose_name='Titulo del Pauqete de servicios')
    sub_intros = RichTextField(blank=True,verbose_name='Informacion general Pauqete servicios')

    back = models.CharField(max_length=150, null=True, blank=True,verbose_name='En que paginas estas?')
    icon= models.CharField(choices=categorias,max_length=150, null=True, blank=True,verbose_name='Elije el icono')
    items = models.CharField(max_length=150, null=True, blank=True,verbose_name='Plan Basico')
    item2 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Plan Premium')
    item3 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Plan Gold')
    item4 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Albanieria')
    item5 = models.CharField(max_length=150, null=True, blank=True,verbose_name='plomeria')
    item6 = models.CharField(max_length=150, null=True, blank=True,verbose_name='electricidad')
    item7 = models.CharField(max_length=150, null=True, blank=True,verbose_name='carpitenria')
    item8 = models.CharField(max_length=150, null=True, blank=True,verbose_name='luminaria')
    item9 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Hidromecanica')
    item10 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Electromecanica')


    certi = models.CharField(max_length=150, null=True, blank=True,verbose_name='Certificado por:')
    city = models.CharField(max_length=150, null=True, blank=True,verbose_name='Ciudad')
    term = RichTextField(blank=True,verbose_name='Informacion legal del servicio')


    promo= models.CharField(choices=colors,max_length=150, null=True, blank=True,verbose_name='Elije el color promocional')
    oferta= models.CharField(choices=ofert,max_length=150, null=True, blank=True,verbose_name='Elije el color promocional')
    promo2= models.CharField(choices=colors,max_length=150, null=True, blank=True,verbose_name='Elije el color promocional')
    oferta2= models.CharField(choices=ofert,max_length=150, null=True, blank=True,verbose_name='Elije el color promocional')
    promo3= models.CharField(choices=colors,max_length=150, null=True, blank=True,verbose_name='Elije el color promocional')
    oferta3= models.CharField(choices=ofert,max_length=150, null=True, blank=True,verbose_name='Elije el color promocional')
    promo4= models.CharField(choices=colors,max_length=150, null=True, blank=True,verbose_name='Elije el color promocional')
    oferta4= models.CharField(choices=ofert,max_length=150, null=True, blank=True,verbose_name='Elije el color promocional')
    promo5= models.CharField(choices=colors,max_length=150, null=True, blank=True,verbose_name='Elije el color promocional')
    oferta5= models.CharField(choices=ofert,max_length=150, null=True, blank=True,verbose_name='Elije el color promocional')
    promo6= models.CharField(choices=colors,max_length=150, null=True, blank=True,verbose_name='Elije el color promocional')
    oferta6= models.CharField(choices=ofert,max_length=150, null=True, blank=True,verbose_name='Elije el color promocional')
    
    promo7= models.CharField(choices=colors,max_length=150, null=True, blank=True,verbose_name='Elije el color promocional')
    oferta7= models.CharField(choices=ofert,max_length=150, null=True, blank=True,verbose_name='Elije el color promocional')
    promo8= models.CharField(choices=colors,max_length=150, null=True, blank=True,verbose_name='Elije el color promocional')
    oferta8= models.CharField(choices=ofert,max_length=150, null=True, blank=True,verbose_name='Elije el color promocional')
    promo9= models.CharField(choices=colors,max_length=150, null=True, blank=True,verbose_name='Elije el color promocional')
    oferta9= models.CharField(choices=ofert,max_length=150, null=True, blank=True,verbose_name='Elije el color promocional')
    promo10= models.CharField(choices=colors,max_length=150, null=True, blank=True,verbose_name='Elije el color promocional')
    oferta10= models.CharField(choices=ofert,max_length=150, null=True, blank=True,verbose_name='Elije el color promocional')


    image = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Imagen de Fondo del Barner-servicios')
    confirmacion = models.CharField( max_length=255,blank=True,null=True ,help_text="El texto de que efectivamente la cotizacion llega pronto")
    thank_you_text = RichTextField(blank=True)
   


    content_panels = AbstractEmailForm.content_panels + Page.content_panels + [
        FieldPanel('intro', classname="full"),
        FieldPanel('sub_intro', classname="full"),
        FieldPanel('icon', classname="full"),

        FieldPanel('introp', classname="full"),
        FieldPanel('sub_introp', classname="full"),

        FieldPanel('items', classname="full"),
        FieldPanel('promo', classname="full"),
        FieldPanel('oferta', classname="full"),

        
        FieldPanel('item2', classname="full"),
        FieldPanel('promo2', classname="full"),
        FieldPanel('oferta2', classname="full"),

        FieldPanel('item3', classname="full"),
        FieldPanel('promo3', classname="full"),
        FieldPanel('oferta3', classname="full"),

        FieldPanel('intros', classname="full"),
        FieldPanel('sub_intros', classname="full"),

        FieldPanel('item4', classname="full"),
        FieldPanel('promo4', classname="full"),
        FieldPanel('oferta4', classname="full"),

      

        FieldPanel('item5', classname="full"),
        FieldPanel('promo5', classname="full"),
        FieldPanel('oferta5', classname="full"),

        FieldPanel('item6', classname="full"),
        FieldPanel('promo6', classname="full"),
        FieldPanel('oferta6', classname="full"),

        FieldPanel('item7', classname="full"),
        FieldPanel('promo7', classname="full"),
        FieldPanel('oferta7', classname="full"),

        FieldPanel('item8', classname="full"),
        FieldPanel('promo8', classname="full"),
        FieldPanel('oferta8', classname="full"),

        FieldPanel('item9', classname="full"),
        FieldPanel('promo9', classname="full"),
        FieldPanel('oferta9', classname="full"),

        FieldPanel('item10', classname="full"),
        FieldPanel('promo10', classname="full"),
        FieldPanel('oferta10', classname="full"),

        FieldPanel('certi', classname="full"),
        FieldPanel('city', classname="full"),
        FieldPanel('term', classname="full"),
        FieldPanel('back', classname="full"),

        InlinePanel('galleria2', label="Imagen de servicios"),
        FieldPanel('confirmacion'),

        FormSubmissionsPanel(),
        InlinePanel('form_fields', label="Form fields"),
        FieldPanel('thank_you_text', classname="full"),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('from_address', classname="col6"),
                FieldPanel('to_address', classname="col6"),
            ]),
            FieldPanel('subject'),
        ], "Email"),
    ]

class Banco_de_imagenes_servicios_mantenimiento(Orderable):
    pageS = ParentalKey(index_servicios_mantenimiento, on_delete=models.CASCADE, related_name='galleria2')
    image = models.ForeignKey('wagtailimages.Image', on_delete=models.CASCADE, related_name='+',verbose_name='Imagen Barner',null=True)
    
    image2 = models.ForeignKey('wagtailimages.Image', on_delete=models.CASCADE, related_name='+',verbose_name='Imagen-plan Basico',null=True)
    image3 = models.ForeignKey('wagtailimages.Image', on_delete=models.CASCADE, related_name='+',verbose_name='Imagen-plan Premium',null=True)
    image4 = models.ForeignKey('wagtailimages.Image', on_delete=models.CASCADE, related_name='+',verbose_name='Imagen-plan de Gold ',null=True)
    image5 = models.ForeignKey('wagtailimages.Image', on_delete=models.CASCADE, related_name='+',verbose_name='Imagen-Albanieria',null=True)
    image6 = models.ForeignKey('wagtailimages.Image', on_delete=models.CASCADE, related_name='+',verbose_name='Imagen-Plomeria',null=True)
    image7 = models.ForeignKey('wagtailimages.Image', on_delete=models.CASCADE, related_name='+',verbose_name='Imagen-Electricidad',null=True)
    image8 = models.ForeignKey('wagtailimages.Image', on_delete=models.CASCADE, related_name='+',verbose_name='Imagen-Carpinteria',null=True)
    image9 = models.ForeignKey('wagtailimages.Image', on_delete=models.CASCADE, related_name='+',verbose_name='Imagen-Luminaria',null=True)
    image10 = models.ForeignKey('wagtailimages.Image', on_delete=models.CASCADE, related_name='+',verbose_name='Imagen-Hidromecanica',null=True)
    image11 = models.ForeignKey('wagtailimages.Image', on_delete=models.CASCADE, related_name='+',verbose_name='Imagen-electromecanica',null=True)

    image_2 = models.ForeignKey('wagtailimages.Image', on_delete=models.CASCADE, related_name='+',verbose_name='Imagen-info plan Basico',null=True)
    image_3 = models.ForeignKey('wagtailimages.Image', on_delete=models.CASCADE, related_name='+',verbose_name='Imagen-info plan Premium',null=True)
    image_4 = models.ForeignKey('wagtailimages.Image', on_delete=models.CASCADE, related_name='+',verbose_name='Imagen-info plan de Gold ',null=True)
    image_5 = models.ForeignKey('wagtailimages.Image', on_delete=models.CASCADE, related_name='+',verbose_name='Imagen-info Albanieria',null=True)
    image_6 = models.ForeignKey('wagtailimages.Image', on_delete=models.CASCADE, related_name='+',verbose_name='Imagen-info Plomeria',null=True)
    image_7 = models.ForeignKey('wagtailimages.Image', on_delete=models.CASCADE, related_name='+',verbose_name='Imagen-info Electricidad',null=True)
    image_8 = models.ForeignKey('wagtailimages.Image', on_delete=models.CASCADE, related_name='+',verbose_name='Imagen-info Carpinteria',null=True)
    image_9 = models.ForeignKey('wagtailimages.Image', on_delete=models.CASCADE, related_name='+',verbose_name='Imagen-info Luminaria',null=True)
    image_10 = models.ForeignKey('wagtailimages.Image', on_delete=models.CASCADE, related_name='+',verbose_name='Imagen-info Hidromecanica',null=True)
    image_11 = models.ForeignKey('wagtailimages.Image', on_delete=models.CASCADE, related_name='+',verbose_name='Imagen-info electromecanica',null=True)
    
    panels = [
        ImageChooserPanel('image'),
        ImageChooserPanel('image2'),
        ImageChooserPanel('image_2'),
        ImageChooserPanel('image3'),
        ImageChooserPanel('image_3'),
        ImageChooserPanel('image4'),
        ImageChooserPanel('image_4'),
        ImageChooserPanel('image5'),
        ImageChooserPanel('image_5'),
        ImageChooserPanel('image6'),
        ImageChooserPanel('image_6'),
        ImageChooserPanel('image7'),
        ImageChooserPanel('image_7'),
        ImageChooserPanel('image8'),
        ImageChooserPanel('image_8'),
        ImageChooserPanel('image9'),
        ImageChooserPanel('image_9'),
        ImageChooserPanel('image10'),
        ImageChooserPanel('image_10'),
        ImageChooserPanel('image11'),
        ImageChooserPanel('image_11'),  
    ]

class FormField3(AbstractFormField):
    page = ParentalKey('index_servicios_revestimiento', on_delete=models.CASCADE, related_name='form_fields')

class index_servicios_revestimiento(AbstractEmailForm):
    
    siren='siren'
    roller='roller'
    lista='list'
    tool='toolbox'

    categorias=[(siren,'siren'),
    (roller,'roller'),
    (lista,'list'),(tool,'toolbox'),
    ]

    primary='primary'
    secundary ='secundary'
    colors=[(primary,'primary'),(secundary ,'secundary')]

    black='Black'
    promocion='Oferta'
    ofert=[(black,'Black'),(promocion,'Oferta')]

    intro = RichTextField(blank=True,verbose_name='Titulo del Barner')
    sub_intro = RichTextField(blank=True,verbose_name='Informacion general')
    back = models.CharField(max_length=150, null=True, blank=True,verbose_name='En que paginas estas?')
    icon= models.CharField(choices=categorias,max_length=150, null=True, blank=True,verbose_name='Elije el icono')

    introap = RichTextField(blank=True,verbose_name='Titulo planes de revestimiento')
    sub_introp = RichTextField(blank=True,verbose_name='Infor planes de revestimiento')

    items = models.CharField(max_length=150, null=True, blank=True,verbose_name='Plan-Ahorro')
    item2 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Plan-Diseno')
    item3 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Plan-corporativo')

    intros = RichTextField(blank=True,verbose_name='Titulo servicios')
    sub_intros = RichTextField(blank=True,verbose_name='Infor servicios')

    introp = RichTextField(blank=True,verbose_name='Titulo servicios')
    sub_introp = RichTextField(blank=True,verbose_name='Infor servicios')

    item4 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Interiores')
    item5 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Exteriores')
    item6 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Acabados')

    certi = models.CharField(max_length=150, null=True, blank=True,verbose_name='Certificado por:')
    city = models.CharField(max_length=150, null=True, blank=True,verbose_name='Ciudad')
    term = RichTextField(blank=True,verbose_name='Informacion legal del servicio')
    promo= models.CharField(choices=colors,max_length=150, null=True, blank=True,verbose_name='Elije el color promocional')
    oferta= models.CharField(choices=ofert,max_length=150, null=True, blank=True,verbose_name='Elije el color promocional')
    promo2= models.CharField(choices=colors,max_length=150, null=True, blank=True,verbose_name='Elije el color promocional')
    oferta2= models.CharField(choices=ofert,max_length=150, null=True, blank=True,verbose_name='Elije el color promocional')
    promo3= models.CharField(choices=colors,max_length=150, null=True, blank=True,verbose_name='Elije el color promocional')
    oferta3= models.CharField(choices=ofert,max_length=150, null=True, blank=True,verbose_name='Elije el color promocional')
    promo4= models.CharField(choices=colors,max_length=150, null=True, blank=True,verbose_name='Elije el color promocional')
    oferta4= models.CharField(choices=ofert,max_length=150, null=True, blank=True,verbose_name='Elije el color promocional')
    promo5= models.CharField(choices=colors,max_length=150, null=True, blank=True,verbose_name='Elije el color promocional')
    oferta5= models.CharField(choices=ofert,max_length=150, null=True, blank=True,verbose_name='Elije el color promocional')
    promo6= models.CharField(choices=colors,max_length=150, null=True, blank=True,verbose_name='Elije el color promocional')
    oferta6= models.CharField(choices=ofert,max_length=150, null=True, blank=True,verbose_name='Elije el color promocional')
    

    image = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Imagen de Fondo del Barner-servicios')
    confirmacion = models.CharField( max_length=255,blank=True,null=True ,help_text="El texto de que efectivamente la cotizacion llega pronto")
    thank_you_text = RichTextField(blank=True)
   


    content_panels = AbstractEmailForm.content_panels + Page.content_panels + [
        FieldPanel('intro', classname="full"),
        FieldPanel('sub_intro', classname="full"),
        FieldPanel('icon', classname="full"),

        FieldPanel('introp', classname="full"),
        FieldPanel('sub_introp', classname="full"),

        FieldPanel('items', classname="full"),
        FieldPanel('promo', classname="full"),
        FieldPanel('oferta', classname="full"),

        FieldPanel('item2', classname="full"),
        FieldPanel('promo2', classname="full"),
        FieldPanel('oferta2', classname="full"),

        FieldPanel('item3', classname="full"),
        FieldPanel('promo3', classname="full"),
        FieldPanel('oferta3', classname="full"),

        FieldPanel('intros', classname="full"),
        FieldPanel('sub_intros', classname="full"),

        FieldPanel('item4', classname="full"),
        FieldPanel('promo4', classname="full"),
        FieldPanel('oferta4', classname="full"),

        FieldPanel('item5', classname="full"),
        FieldPanel('promo5', classname="full"),
        FieldPanel('oferta5', classname="full"),

        FieldPanel('item6', classname="full"),
        FieldPanel('promo6', classname="full"),
        FieldPanel('oferta6', classname="full"),

        FieldPanel('certi', classname="full"),
        FieldPanel('city', classname="full"),
        FieldPanel('term', classname="full"),
        FieldPanel('back', classname="full"),

        InlinePanel('galleria2', label="Imagen de servicios"),
        FieldPanel('confirmacion'),

        FormSubmissionsPanel(),
        InlinePanel('form_fields', label="Form fields"),
        FieldPanel('thank_you_text', classname="full"),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('from_address', classname="col6"),
                FieldPanel('to_address', classname="col6"),
            ]),
            FieldPanel('subject'),
        ], "Email"),
    ]

class Banco_de_imagenes_servicios_revestimiento(Orderable):
    pageS = ParentalKey(index_servicios_revestimiento, on_delete=models.CASCADE, related_name='galleria2')
    image = models.ForeignKey('wagtailimages.Image', on_delete=models.CASCADE, related_name='+',verbose_name='Imagen Barner',null=True)
    
    image2 = models.ForeignKey('wagtailimages.Image', on_delete=models.CASCADE, related_name='+',verbose_name='Imagen-plan de Ahorro',null=True)
    image_2 = models.ForeignKey('wagtailimages.Image', on_delete=models.CASCADE, related_name='+',verbose_name='Imagen-info plan de Ahorro',null=True)
    image3 = models.ForeignKey('wagtailimages.Image', on_delete=models.CASCADE, related_name='+',verbose_name='Imagen- plan de Diseno',null=True)
    image_3 = models.ForeignKey('wagtailimages.Image', on_delete=models.CASCADE, related_name='+',verbose_name='Imagen- info plan de Diseno',null=True)
    image4 = models.ForeignKey('wagtailimages.Image', on_delete=models.CASCADE, related_name='+',verbose_name='Imagen- plan de Corporativo',null=True) 
    image_4 = models.ForeignKey('wagtailimages.Image', on_delete=models.CASCADE, related_name='+',verbose_name='Imagen-info plan de Corporativo',null=True)
    image5 = models.ForeignKey('wagtailimages.Image', on_delete=models.CASCADE, related_name='+',verbose_name='interiores',null=True)       
    image_5 = models.ForeignKey('wagtailimages.Image', on_delete=models.CASCADE, related_name='+',verbose_name='info-interiores',null=True)
    image6 = models.ForeignKey('wagtailimages.Image', on_delete=models.CASCADE, related_name='+',verbose_name='acabados',null=True)
    image_6 = models.ForeignKey('wagtailimages.Image', on_delete=models.CASCADE, related_name='+',verbose_name='info acabados',null=True)
    image7 = models.ForeignKey('wagtailimages.Image', on_delete=models.CASCADE, related_name='+',verbose_name='exteriores',null=True)
    image_7 = models.ForeignKey('wagtailimages.Image', on_delete=models.CASCADE, related_name='+',verbose_name='info exteriores',null=True)
   
    panels = [
        ImageChooserPanel('image'),
        ImageChooserPanel('image2'),
        ImageChooserPanel('image_2'),
        ImageChooserPanel('image3'),
        ImageChooserPanel('image_3'),
        ImageChooserPanel('image4'),
        ImageChooserPanel('image_4'),
        ImageChooserPanel('image5'),
        ImageChooserPanel('image_5'),
        ImageChooserPanel('image6'),
        ImageChooserPanel('image_6'),
        ImageChooserPanel('image7'),
        ImageChooserPanel('image_7'),    
    ]

# Pagina de servicios

class contacto(AbstractFormField):
    page = ParentalKey('servicios', on_delete=models.CASCADE, related_name='form_fields')

class servicios(AbstractEmailForm):

    title2 = RichTextField(blank=True,verbose_name='Titulo de la pagina')
    intro = RichTextField(blank=True,verbose_name='Titulo del Barner')
    intro2 = RichTextField(blank=True,verbose_name='Subtitulo del Barner ')
    intro3 = RichTextField(blank=True,verbose_name='Introduccion al servicio ')
    intro4 = RichTextField(blank=True,verbose_name='Descripcion del servicio')
    intro5 = RichTextField(blank=True,verbose_name='Descripcion del servicio-debajo de la imagen')
    intro6 = RichTextField(blank=True,verbose_name='Nombre de Promain')
    intro7 = RichTextField(blank=True,verbose_name='Comentario de Promain')

    list1 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Nombre de lista de productos')
    item = models.CharField(max_length=150, null=True, blank=True,verbose_name='item1')
    unit= models.IntegerField(null=True, blank=True,verbose_name='Costo del Item 1')
    item2 = models.CharField(max_length=150, null=True, blank=True,verbose_name='item2')
    unit2= models.IntegerField(null=True, blank=True,verbose_name='Costo del Item 2')
    item3 = models.CharField(max_length=150, null=True, blank=True,verbose_name='item3')
    unit3= models.IntegerField(null=True, blank=True,verbose_name='Costo del Item 3')
    item4 = models.CharField(max_length=150, null=True, blank=True,verbose_name='item4')
    unit4= models.IntegerField(null=True, blank=True,verbose_name='Costo del Item 4')
    item5 = models.CharField(max_length=150, null=True, blank=True,verbose_name='item5')
    unit5= models.IntegerField(null=True, blank=True,verbose_name='Costo del Item 5')
    item6 = models.CharField(max_length=150, null=True, blank=True,verbose_name='item6')
    unit6= models.IntegerField(null=True, blank=True,verbose_name='Costo del Item 6')
    item7 = models.CharField(max_length=150, null=True, blank=True,verbose_name='item7')
    unit7= models.IntegerField(null=True, blank=True,verbose_name='Costo del Item 7')
    item8 = models.CharField(max_length=150, null=True, blank=True,verbose_name='item8')
    unit8= models.IntegerField(null=True, blank=True,verbose_name='Costo del Item 8')
    item9 = models.CharField(max_length=150, null=True, blank=True,verbose_name='item9')
    unit9 = models.IntegerField(null=True, blank=True,verbose_name='Costo del Item 9')
    item10 = models.CharField(max_length=150, null=True, blank=True,verbose_name='item10')
    unit10 = models.IntegerField(null=True, blank=True,verbose_name='Costo del Item 10')
    term = RichTextField(blank=True,verbose_name='Garantias, terminos y condiciones')
    thank_you_text = RichTextField(blank=True)
  

    content_panels = Page.content_panels + AbstractEmailForm.content_panels + [
        FieldPanel('title2', classname="full"),
        FieldPanel('intro', classname="full"),
        FieldPanel('intro2', classname="full"),
        FieldPanel('intro3', classname="full"),
        FieldPanel('intro4', classname="full"),
        FieldPanel('intro5', classname="full"),
        FieldPanel('intro6', classname="full"),
        FieldPanel('intro7', classname="full"),
        FieldPanel('list1', classname="full"),
        FieldPanel('item', classname="full"),
        FieldPanel('unit', classname="full"),
        FieldPanel('item2', classname="full"),
        FieldPanel('unit2', classname="full"),
        FieldPanel('item3', classname="full"),
        FieldPanel('unit3', classname="full"),
        FieldPanel('item4', classname="full"),
        FieldPanel('unit4', classname="full"),
        FieldPanel('item5', classname="full"),
        FieldPanel('unit5', classname="full"),
        FieldPanel('item6', classname="full"),
        FieldPanel('unit6', classname="full"),
        FieldPanel('item7', classname="full"),
        FieldPanel('unit7', classname="full"),
        FieldPanel('item8', classname="full"),
        FieldPanel('unit8', classname="full"),
        FieldPanel('item9', classname="full"),
        FieldPanel('unit9', classname="full"),
        FieldPanel('item10', classname="full"),
        FieldPanel('unit10', classname="full"),
        InlinePanel('galleria3', label="Imagen de Fondo Barner"),

        FormSubmissionsPanel(),
        InlinePanel('form_fields', label="contacto"),
        FieldPanel('thank_you_text', classname="full"),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('from_address', classname="col6"),
                FieldPanel('to_address', classname="col6"),
            ]),
            FieldPanel('subject'),
        ], "Email"),

        ]

class GaleriadeImagenesservicios(Orderable):
    page = ParentalKey(servicios, on_delete=models.CASCADE, related_name='galleria3')
    image = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Imagen de Fondo del Barner')
    image2 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Imagen del servicio')
    image3 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto-ProMain')

    panels = [
        ImageChooserPanel('image'),
        ImageChooserPanel('image2'),
        ImageChooserPanel('image3'),
        ]

# Pagina de Buscar empleo

class jobs_formulario(AbstractFormField):
    page = ParentalKey('jobs', on_delete=models.CASCADE, related_name='jobs_formulario')

class jobs(AbstractEmailForm):
    title3 = RichTextField(blank=True,verbose_name='Titulo del barner')
    intro2 = RichTextField(blank=True,verbose_name='Subtitulo del Barner ')
    
    intro3= models.CharField(max_length=150, null=True, blank=True,verbose_name='Titulo de trabajos')
    infojobs = RichTextField(blank=True,verbose_name='Informacion de trabajo descriptivo ')
    infojobs2 = RichTextField(blank=True,verbose_name='Informacion de trabajo descriptivo debajo de la imagen ')
    intro4= models.CharField(max_length=150, null=True, blank=True,verbose_name='Nombre del acesor')
    intro5= models.CharField(max_length=150, null=True, blank=True,verbose_name='Info del acesor')
    term= RichTextField(blank=True,verbose_name='Terminos de aplicacion de trabajo')
    thank_you_text = RichTextField(blank=True)

    


    content_panels = Page.content_panels + AbstractEmailForm.content_panels + [
        FieldPanel('title3', classname="full"),
        FieldPanel('intro2', classname="full"),
        FieldPanel('intro3', classname="full"),
        FieldPanel('intro4', classname="full"),
        FieldPanel('intro5', classname="full"),
        FieldPanel('term', classname="full"),

        FieldPanel('infojobs', classname="full"),
        FieldPanel('infojobs2', classname="full"),

        InlinePanel('galleria4', label="Imagenes"),

        FormSubmissionsPanel(),
        InlinePanel('jobs_formulario', label="formulario de trabajo"),
        FieldPanel('thank_you_text', classname="full"),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('from_address', classname="col6"),
                FieldPanel('to_address', classname="col6"),
            ]),
            FieldPanel('subject'),
        ], "Email"),
    ]
class GaleriadeImagenesjobs(Orderable):
    page = ParentalKey(jobs, on_delete=models.CASCADE, related_name='galleria4')
    image = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Imagen de Fondo del Barner-jobs')
    image2 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Imagen de Trabajos')
    image3 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto del acesor admnistrativo')
    panels = [
        ImageChooserPanel('image'),
        ImageChooserPanel('image2'),
        ImageChooserPanel('image3'),
        ]

# Pagina de ProMTF


class ProMTFpage(Page):
    title3 = RichTextField(blank=True,verbose_name='Titulo del barner-ProMTF')
    intro2 = RichTextField(blank=True,verbose_name='Subtitulo del Barner-ProMTF ')
    
    intro3= models.CharField(max_length=150, null=True, blank=True,verbose_name='Titulo de ProMTF')
    infojobs = RichTextField(blank=True,verbose_name='Informacion de  ProMTF descriptivo ')
    infojobs2 = RichTextField(blank=True,verbose_name='Informacion de ProMTF descriptivo debajo de la imagen ')
    intro4= models.CharField(max_length=150, null=True, blank=True,verbose_name='Nombre del acesor')
    intro5= models.CharField(max_length=150, null=True, blank=True,verbose_name='Info del acesor')
    term= RichTextField(blank=True,verbose_name='Mensaje para que los ProMTF apliquen')

    

    content_panels = Page.content_panels + [
        FieldPanel('title3', classname="full"),
        FieldPanel('intro2', classname="full"),
        FieldPanel('intro3', classname="full"),
        FieldPanel('intro4', classname="full"),
        FieldPanel('intro5', classname="full"),
        FieldPanel('term', classname="full"),

        FieldPanel('infojobs', classname="full"),
        FieldPanel('infojobs2', classname="full"),

        InlinePanel('galleria5', label="Imagenes"),
    ]

class GaleriadeImagenesProMain(Orderable):
    page = ParentalKey(ProMTFpage, on_delete=models.CASCADE, related_name='galleria5')
    image = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Imagen de Fondo del Barner-ProMTF')
    image2 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Imagen de ProMTF-publicidad')
    image3 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto del acesor admnistrativo')

    panels = [
        ImageChooserPanel('image'),
        ImageChooserPanel('image2'),
        ImageChooserPanel('image3'),
        ]










