from django.conf.urls.static import static
from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from home.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("home.urls")),
    path("accounts/", include("django.contrib.auth.urls"))]

#Destinar imagenes a carpeta 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)