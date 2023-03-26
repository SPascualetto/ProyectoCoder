from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('AppCoder.urls')),
    path('registro/', include('django.contrib.auth.urls')),
    path('registro/', include('registro.urls')),
    
]
