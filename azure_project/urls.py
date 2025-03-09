from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('azure_content.urls')),
    path("sensor/", include("sensor_app.urls")),
]
