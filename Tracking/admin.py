from django.contrib import admin
from .models import Company, Employee, Device, DeviceLog, Staff
# Register your models here.
admin.site.register(Company)
admin.site.register(Employee)
admin.site.register(Device)
admin.site.register(DeviceLog)
admin.site.register(Staff)
