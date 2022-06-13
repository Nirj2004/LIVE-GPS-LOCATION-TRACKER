from django.contrib import admin
from .models import DeviceLocation
class DeviceLocationModelAdmin(admin.ModelAdmin):
    list_display = ['deviceIdD', 'lat', 'long', 'speed', 'accuracy', 'timestamp']
    class Meta:
        model = DeviceLocation
admin.site.register(DeviceLocation, DeviceLocationModelAdmin)
