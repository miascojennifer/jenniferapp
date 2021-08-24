
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('TUPConline_appointment.urls')),
    path('admin/', admin.site.urls),
    
]
