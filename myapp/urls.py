from django.urls import path
from .views import home,upload
from . import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('',home),
    path('upload/',upload),
] + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT )
