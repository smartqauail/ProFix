from django.urls import path,re_path,include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy as _
from noticias.sitemaps import PostSitemap

from baton.autodiscover import admin

from wagtail.admin import urls as wagtailadmin_urls
from wagtail.core import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls

sitemaps = {
    'posts': PostSitemap,
}

urlpatterns = i18n_patterns(

    path(_('profixadmin/'), admin.site.urls),
    path(_('account/'), include('account.urls')),
    path(_('baton/'),include('baton.urls')),
    path(_('noticias/'), include('noticias.urls', namespace='noticias')),
    path(_('sitemap.xml'), sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    
    path(_('social-auth/'), include('social_django.urls', namespace='social')),
    path(_('images/'), include('images.urls', namespace='images')),
    path(_('cart/'), include('cart.urls', namespace='cart')),
    path(_('orders/'), include('orders.urls', namespace='orders')),
    path(_('Avadell/'), include('Avadell.urls', namespace='avadell')),
    path(_('payment/'), include('payment.urls', namespace='payment')),
    path(_('rosetta/'),include('rosetta.urls')),
    path(_('shop/'), include('shop.urls', namespace='shop')),
    
    re_path(r'^profixcms/', include(wagtailadmin_urls)),
    re_path(r'^documents/', include(wagtaildocs_urls)),
    re_path(r'', include(wagtail_urls)),
 ) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# si Debug=True, reemplazamos con el siguiente codigo

 #if settings.DEBUG:
     #urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)