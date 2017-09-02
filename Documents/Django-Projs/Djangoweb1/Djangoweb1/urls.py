
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$', include('Home.urls',namespace = 'Home')),
    url(r'^admin/', admin.site.urls),
    url(r'^Music/', include('Music.urls',namespace = 'Music')),
    url(r'^Accounts/', include('Accounts.urls',namespace = 'Accounts')),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT )
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
