from django.contrib import admin
from django.urls import path
from cifrar import views as cifrar_views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cifrar/', cifrar_views.cifrado, name="cypher")
] + static(settings.STATIC_URL)
