from django.contrib import admin
from django.urls import path, include
from core.views import index, who_we_are, portfolio, services, products, contactus


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('api-auth/', include('rest_framework.urls'))
]


