

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '7$^)g^hch*#-kka0uq@=2p_fo-1gws_ax09a(xxb3*+#_=+i_h'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

TEMPLATE_DIR = os.path.join(BASE_DIR,"templates")
MEDIA_URL = '/media/'
STATIC_URL = '/static/'
WAGTAIL_SITE_NAME = 'ProFix CMS'

ALLOWED_HOSTS = [
    'mysite.com',
    'localhost',
    '127.0.0.1',
    '3f6ad53c.ngrok.io'
]

#Email setups
EMAIL_HOST          = 'smtp.gmail.com'
EMAIL_PORT          = 587
EMAIL_HOST_USER     = 'profixmainhousing@gmail.com'
EMAIL_HOST_PASSWORD = 'aewgajdobewqvkba'
EMAIL_USE_TLS       = True
DEFAULT_FROM_EMAIL  = EMAIL_HOST_USER
EMAIL_BACKEND       = 'django.core.mail.backends.smtp.EmailBackend'

# Redireccionamiento de entradas y salidas de usuarios

LOGIN_REDIRECT_URL='Dashboard'
LOGIN_URL='login'
LOGOUT_URL='logout'

# Application definition

INSTALLED_APPS = [
    
    'baton',
    #'djmoney',
    #'account',
    'django.contrib.admin',
    'django_humanize',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
   
    

    'wagtail.contrib.forms',
    'wagtail.contrib.redirects',
    'wagtail.contrib.styleguide',
    'wagtail.embeds',
    'wagtail.sites',
    'wagtail.users',
    'wagtail.snippets',
    'wagtail.documents',
    'wagtail.images',
    'wagtail.search',
    'widget_tweaks',
    'bootstrap4',
    'core',   
    'wagtail.admin',
    'wagtail.core',

#ProFixApps
    'images',
    'actions',
    'profixinvoice',
    'noticias',
    'ProFixFWW',
    'coupons',
    'ProMain',
    'payment',
    'cart',
    'orders',
    'profixdatabase',
    'profixprojects',

    'shop',
    'profit',
#Profits-Associados
    'Avadell',
#ProMAins-Asociados

#ProCrew

    'modelcluster',
    'social_django',
    'sorl.thumbnail',
    'taggit',
    'mathfilters',
    

    'phone_field',
    'django.contrib.sitemaps',
    'django.contrib.postgres',
    'rosetta',
    'parler',
    'localflavor',
    
    'baton.autodiscover',    
]



BATON = {
    'SITE_HEADER': ' &ensp;  &ensp;  <img src="/static/profix_logo.png" height="44px"></a>',
    'SITE_TITLE': 'ProFix|Maintenece Housing',
    'INDEX_TITLE': 'Sistemas de Mantenimientos Estructurales',
    'SUPPORT_HREF': 'https://github.com/otto-torino/django-baton/issues',
    'COPYRIGHT': ' <a href="https://www.otto.to.it"><h1><img src="/static/inst.png" height="20px"><img src="/static/face.png" height="20px"><img src="/static/twiter.png" height="20px"><img src="/static/in.png" height="20px"><img src="/static/whats.png" height="20px"></h1></a><h6>Quito-Ecuador <h9>copyright © 2020</h9></h6> ', # noqa
    'POWERED_BY': '<a href="https://www.otto.to.it"><img src="/static/logo2.png" height="30px"></a>',
    'CONFIRM_UNSAVED_CHANGES': True,
    'SHOW_MULTIPART_UPLOADING': True,
    'ENABLE_IMAGES_PREVIEW': True,
    'MENU': (
        { 'type': 'title', 'label': 'ProFix-Admin', 'apps': ('auth','noticias', ) },
        {
            'type': 'app',
            'name': 'auth',
            'label': 'Proyectos',
            'icon': 'fa fa-flask ',
            'models': (
                {
                    'name': 'user',
                    'label': 'Registro'
                },
                {
                    'name': 'group',
                    'label': 'Cotizaciones'
                },
                 {
                    'name': 'group',
                    'label': 'Facturación',
                },
            )
        },
        {
            'type': 'app',
            'name': 'auth',
            'label': 'Documentos',
            'icon': 'fa  fa-book  ',
            'models': (
                {
                    'name': 'user',
                    'label': 'Reportes-ProFix'
                },
                {
                    'name': 'group',
                    'label': 'Informes-ProFix'
                },
                 {
                    'name': 'group',
                    'label': 'Reportes-ProMAin'
                },
                   {
                    'name': 'group',
                    'label': 'Informes-ProMain'
                },
                 {
                    'name': 'group',
                    'label': 'Actas de Entrega'
                },
            )
        },
         {
            'type': 'app',
            'name': 'profit',
            'label': 'ProFit',
            'icon': 'fa fa-building ',
            'models': (
                {
                    'name': 'edificio',
                    'label': 'Edificios'
                },
                 {
                    'name': 'profile',
                    'label': 'Colegios y Universidades'
                },
                 {
                    'name': 'profile',
                    'label': 'Hospitales'
                },
                 {
                    'name': 'profile',
                    'label': 'Casas y Departamentos'
                }, 
                
                )
        },
          {
            'type': 'app',
            'name': 'coupons',
            'label': 'ProMain',
            'icon': 'fa fa-user-circle',
            'models': (
                {
                    'name': 'coupon',
                    'label': 'Proveedores'
                },
                   {
                    'name': 'coupon',
                    'label': 'Cotizaciones'
                },
                   {
                    'name': 'coupon',
                    'label': 'Plan de Trabajo'
                },
                {
                    'name': 'coupon',
                    'label': 'Liquidaciones'
                },
                
                )
        },
         {
            'type': 'app',
            'name': 'coupons',
            'label': 'ProTools',
            'icon': 'fa fa-cogs',
            'models': (
                  {
                    'name': 'coupon',
                    'label': 'Proveedores'
                },
                   {
                    'name': 'coupon',
                    'label': 'Cotizaciones'
                },
                   {
                    'name': 'coupon',
                    'label': 'Plan de Trabajo'
                },
                {
                    'name': 'coupon',
                    'label': 'Liquidaciones'
                },
            )
        },

         {
            'type': 'app',
            'name': 'auth',
            'label': 'ProCrew',
            'icon': 'fa fa-users',
            'models': (
                {
                    'name': 'user',
                    'label': 'Usuarios'
                },
                {
                    'name': 'group',
                    'label': 'Equipos'
                },
            )
        },

            {
            'type': 'app',
            'name': 'auth',
            'label': 'Agenda ProFix',
            'icon': 'fa fa-calendar-check',
            'models': (
                {
                    'name': 'user',
                    'label': 'Presidencia'
                },
                {
                    'name': 'group',
                    'label': 'Gerencia'
                },
                   {
                    'name': 'group',
                    'label': 'Administración'
                },
            )
        },

        {
            'type': 'app',
            'name': 'auth',
            'label': 'Archivo',
            'icon': 'fa fa-archive ',
            'models': (
                {
                    'name': 'user',
                    'label': 'Actas'
                },
                {
                    'name': 'group',
                    'label': 'Cotizaciones'
                },
                {
                    'name': 'group',
                    'label': 'Facturas-ProFix'
                },
                {
                    'name': 'group',
                    'label': 'Facturas-ProMain'
                },
                 {
                    'name': 'group',
                    'label': 'Facturas-ProTools'
                },
            )
        },
         {
            'type': 'app',
            'name': 'auth',
            'label': 'Estadisticas',
            'icon': 'fa fa-signal',
            'models': (
                {
                    'name': 'user',
                    'label': 'Proyecciones'
                },
                {
                    'name': 'group',
                    'label': 'Utilidades'
                },
                {
                    'name': 'group',
                    'label': 'Utilidades'
                },
            )
        },

        {
            'type': 'app',
            'name': 'auth',
            'label': 'Contabilidad',
            'icon': 'fa fa-list',
            'models': (
                {
                    'name': 'user',
                    'label': 'Egresos'
                },
                {
                    'name': 'group',
                    'label': 'Ingresos'
                },
                {
                    'name': 'group',
                    'label': 'SRI'
                },
            )
        },

         {
            'type': 'app',
            'name': 'auth',
            'label': 'Legal ProFix',
            'icon': 'fa fa-university',
            'models': (
                {
                    'name': 'user',
                    'label': 'Estatuto'
                },
                {
                    'name': 'group',
                    'label': 'Contratos'
                },
                   {
                    'name': 'group',
                    'label': 'Procedimientos'
                },
            )
        },

        { 'type': 'title', 'label': 'ProFit App', 'apps': ('auth','noticias','Alcala2', ) },
        {
            'type': 'app',
            'name': 'alcala2',
            'label': 'Edificio Alcala2',
            'icon': 'fa fa-building ',
            'models': (
                {
                    'name': 'perfil',
                    'label': 'Informacion'
                },
                {
                    'name': 'diagnostico',
                    'label': 'Diagnostico'
                },
                 {
                    'name': 'diagnostico',
                    'label': 'Proyectos',
                },
                  {
                    'name': 'diagnostico',
                    'label': 'Cotizaciones',
                },
                  {
                    'name': 'diagnostico',
                    'label': 'Liquidaciones',
                },
                   {
                    'name': 'diagnostico',
                    'label': 'Calificación',
                },
                  {
                    'name': 'diagnostico',
                    'label': 'Actas',
                },
            )
        },
        {
            'type': 'app',
            'name': 'asiel',
            'label': 'Edificio Asiel',
            'icon': 'fa  fa-building  ',
            'models': (
                {
                    'name': 'perfil',
                    'label': 'Informacion'
                },
                {
                    'name': 'group',
                    'label': 'Informes-ProFix'
                },
                 {
                    'name': 'group',
                    'label': 'Reportes-ProMAin'
                },
                   {
                    'name': 'group',
                    'label': 'Informes-ProMain'
                },
                 {
                    'name': 'group',
                    'label': 'Actas de Entrega'
                },
            )
        },
         {
            'type': 'app',
            'name': 'profit',
            'label': 'ProFit',
            'icon': 'fa fa-building ',
            'models': (
                {
                    'name': 'edificio',
                    'label': 'Edificios'
                },
                 {
                    'name': 'profile',
                    'label': 'Colegios y Universidades'
                },
                 {
                    'name': 'profile',
                    'label': 'Hospitales'
                },
                 {
                    'name': 'profile',
                    'label': 'Casas y Departamentos'
                }, 
                
                )
        },
          {
            'type': 'app',
            'name': 'coupons',
            'label': 'ProMain',
            'icon': 'fa fa-user-circle',
            'models': (
                {
                    'name': 'coupon',
                    'label': 'Proveedores'
                },
                   {
                    'name': 'coupon',
                    'label': 'Cotizaciones'
                },
                   {
                    'name': 'coupon',
                    'label': 'Plan de Trabajo'
                },
                {
                    'name': 'coupon',
                    'label': 'Liquidaciones'
                },
                
                )
        },
         {
            'type': 'app',
            'name': 'coupons',
            'label': 'ProTools',
            'icon': 'fa fa-cogs',
            'models': (
                  {
                    'name': 'coupon',
                    'label': 'Proveedores'
                },
                   {
                    'name': 'coupon',
                    'label': 'Cotizaciones'
                },
                   {
                    'name': 'coupon',
                    'label': 'Plan de Trabajo'
                },
                {
                    'name': 'coupon',
                    'label': 'Liquidaciones'
                },
            )
        },

         {
            'type': 'app',
            'name': 'auth',
            'label': 'ProCrew',
            'icon': 'fa fa-users',
            'models': (
                {
                    'name': 'user',
                    'label': 'Usuarios'
                },
                {
                    'name': 'group',
                    'label': 'Equipos'
                },
            )
        },

            {
            'type': 'app',
            'name': 'auth',
            'label': 'Agenda ProFix',
            'icon': 'fa fa-calendar-check',
            'models': (
                {
                    'name': 'user',
                    'label': 'Presidencia'
                },
                {
                    'name': 'group',
                    'label': 'Gerencia'
                },
                   {
                    'name': 'group',
                    'label': 'Administración'
                },
            )
        },

        {
            'type': 'app',
            'name': 'auth',
            'label': 'Archivo',
            'icon': 'fa fa-archive ',
            'models': (
                {
                    'name': 'user',
                    'label': 'Actas'
                },
                {
                    'name': 'group',
                    'label': 'Cotizaciones'
                },
                {
                    'name': 'group',
                    'label': 'Facturas-ProFix'
                },
                {
                    'name': 'group',
                    'label': 'Facturas-ProMain'
                },
                 {
                    'name': 'group',
                    'label': 'Facturas-ProTools'
                },
            )
        },
         {
            'type': 'app',
            'name': 'auth',
            'label': 'Estadisticas',
            'icon': 'fa fa-signal',
            'models': (
                {
                    'name': 'user',
                    'label': 'Proyecciones'
                },
                {
                    'name': 'group',
                    'label': 'Utilidades'
                },
                {
                    'name': 'group',
                    'label': 'Utilidades'
                },
            )
        },

        {
            'type': 'app',
            'name': 'auth',
            'label': 'Contabilidad',
            'icon': 'fa fa-list',
            'models': (
                {
                    'name': 'user',
                    'label': 'Egresos'
                },
                {
                    'name': 'group',
                    'label': 'Ingresos'
                },
                {
                    'name': 'group',
                    'label': 'SRI'
                },
            )
        },

         {
            'type': 'app',
            'name': 'auth',
            'label': 'Legal ProFix',
            'icon': 'fa fa-university',
            'models': (
                {
                    'name': 'user',
                    'label': 'Estatuto'
                },
                {
                    'name': 'group',
                    'label': 'Contratos'
                },
                   {
                    'name': 'group',
                    'label': 'Procedimientos'
                },
            )
        },
        { 'type': 'free', 'label': 'Edificios', 'children': [
            { 'type': 'model', 'label': 'Info', 'name': 'perfil', 'app':'alcala2', 'icon': 'fa fa-gavel' },
            { 'type': 'free', 'label': 'Another custom link', 'url': 'http://www.˓→google.it' },
            ]
        },


         
        
      

        { 'type': 'title', 'label': 'FrameWork-Web', 'apps': ('auth','noticias', ) },
         {
            'type': 'app',
            'name': 'account',
            'label': 'Clientes Web',
            'icon': 'fa fa-user',
            'models': (
                {
                    'name': 'profile',
                    'label': 'Cuentas Clientes'
                },
                
                )
        },
          {
            'type': 'app',
            'name': 'coupons',
            'label': 'Promociones',
            'icon': 'fa fa-tag',
            'models': (
                {
                    'name': 'coupon',
                    'label': 'Cupones de Descuento'
                },
                
                )
        },
        
         {
            'type': 'app',
            'name': 'noticias',
            'label': 'Noticias',
            'icon': 'fa fa-globe',
            'models': (
                {
                    'name': 'post',
                    'label': 'Escribir Noticia'
                },
                {
                    'name': 'comment',
                    'label': 'Comentarios'
                },
            )
        },

        {
            'type': 'app',
            'name': 'taggit',
            'label': 'Etiquetas',
            'icon': 'fa fa-tags',
            'models': (
                {
                    'name': 'etiquetas',
                    'label': 'Etiquetas Noticias'
                },
                {
                    'name': 'comment',
                    'label': 'Comentarios'
                },
            )
        },
        


        { 'type': 'title', 'label': 'Contents', 'apps': ('flatpages', ) },
        { 'type': 'model', 'label': 'Pages', 'name': 'flatpage', 'app': 'flatpages' },
        { 'type': 'free', 'label': 'ProFix-Webs','icon': 'fa fa-code ', 'children': [
            { 'type': 'model', 'label': 'A Model', 'name': 'mymodelname', 'app': 'myapp', 'icon': 'fa fa-code ' },
            { 'type': 'free', 'label': 'Noticias', 'url': 'http://127.0.0.1:8000/noticias' },
        ] },

         { 'type': 'title', 'label': 'Mantenimiento-Web', 'apps': ('auth','noticias', ) },
        {
            'type': 'app',
            'name': 'actions',
            'label': 'Registro clientes',
            'icon': 'fa fa-user',
            'models': (
                {
                    'name': 'action',
                    'label': 'Logs clientes webs'
                },
               
            )
        },

          {
            'type': 'app',
            'name': 'orders',
            'label': 'Compras Online',
            'icon': 'fa fa-credit-card',
            'models': (
                {
                    'name': 'order',
                    'label': 'Lista de proyectos-web',
                },
               
            )
        },

         {
            'type': 'app',
            'name': 'shop',
            'label': 'Catalogo de ventas',
            'icon': 'fa fa-map',
            'models': (
                {
                    'name': 'category',
                    'label': 'Categorias de Mantenimiento'
                },
                  {
                    'name': 'product',
                    'label': 'Servicios de Mantenimiento'
                },
                
                )
        },
          {
            'type': 'app',
            'name': 'social_django',
            'label': 'Inrteracciones sociales',
            'icon': 'fa fa-tag',
            'models': (
                {
                    'name': 'Associations ',
                    'label': 'Asociaciones'
                },
                
                )
        },
        {
            'type': 'app',
            'name': 'images',
            'label': 'ProFix Play',
            'icon': 'fa fa-play ',
            'models': (
                {
                    'name': 'image',
                    'label': 'Imagenes de clientes'
                },
                {
                    'name': 'group',
                    'label': 'Equipos'
                },
            )
        },
         {
            'type': 'app',
            'name': 'noticias',
            'label': 'Noticias ProFix',
            'icon': 'fa fa-globe',
            'models': (
                {
                    'name': 'post',
                    'label': 'Escribir Noticia'
                },
                {
                    'name': 'comment',
                    'label': 'Comentarios'
                },
            )
        },
        { 'type': 'title', 'label': 'Contents', 'apps': ('flatpages', ) },
        { 'type': 'model', 'label': 'Pages', 'name': 'flatpage', 'app': 'flatpages' },
        { 'type': 'free', 'label': 'Custom Link', 'url': 'http://www.google.it', 'perms': ('flatpages.add_flatpage', 'auth.change_user') },
        { 'type': 'free', 'label': 'My parent voice', 'children': [
            { 'type': 'model', 'label': 'A Model', 'name': 'mymodelname', 'app': 'myapp', 'icon': 'fa fa-gavel' },
            { 'type': 'free', 'label': 'Another custom link', 'url': 'http://www.google.it' },
        ] },
    ),
}


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'wagtail.core.middleware.SiteMiddleware',
    'wagtail.contrib.redirects.middleware.RedirectMiddleware',
]

PARLER_DEFAULT_LANGUAGE_CODE = 'es'

PARLER_LANGUAGES = {
    None: (
        {'code': 'en'},
        {'code': 'es'},
    ),
    'default': {
        'fallback': 'en',
        'hide_untranslated': False,
    }
}
ROOT_URLCONF = 'ProFix.urls'
SITE_ID=1
CART_SESSION_ID = 'cart'



AUTHENTICATION_BACKENDS=[
    'django.contrib.auth.backends.ModelBackend',
    'account.authentication.EmailAuthBackend',
    'social_core.backends.facebook.FacebookOAuth2',
]

SOCIAL_AUTH_FACEBOOK_KEY = '712585166237152'
SOCIAL_AUTH_FACEBOOK_SECRET='fcbf225cca76b78283d250cb01e13ac2'
SOCIAL_AUTH_FACEBOOK_SCOPE=['email']

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'cart.context_processors.cart',
            ],
        },
    },
]

WSGI_APPLICATION = 'ProFix.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'profixdb',
        'USER': 'profixadmin',
        'PASSWORD': '95355672',
        'HOST':'profix-1702.postgres.pythonanywhere-services.com',
        'PORT':'11702',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/
from django.utils.translation import gettext_lazy as _

LANGUAGES = (
    ('en', _('English')),
    ('es', _('Spanish')),
)

LANGUAGE_CODE = 'en'

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale/'),
)
PHONENUMBER_DB_FORMAT= 'RFC3966'


TIME_ZONE = 'America/Guayaquil'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/


STATICFILES_DIRS = [ os.path.join(BASE_DIR, "static"),'/var/www/static/',]

# Redis settings
REDIS_HOST = 'localhost'
REDIS_PORT = 6379
REDIS_DB = 0
