from django.conf.urls import include, url
from django.contrib import admin
#################
from django.conf import settings
from django.conf.urls.static import static
from sistemaHuellas.views import visor

urlpatterns = [
    # Examples:
    # url(r'^$', 'puertaHuella.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^visor/$',visor),
    url(r'^admin/', include(admin.site.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
