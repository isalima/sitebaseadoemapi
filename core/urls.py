from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from .views import index, who_we_are, portfolio, services, products, contactus

urlpatterns = [
                  path('', index),
                  path('who_we_are', who_we_are),
                  path('services', services),
                  path('products', products),
                  path('contactus', contactus),
                  path('portfolio', portfolio),
                  path('ckeditor', include('ckeditor_uploader.urls'))
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
