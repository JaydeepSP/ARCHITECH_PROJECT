from django.contrib import admin
from .models import AccountData,DesignData,AppointmentData,contactform

admin.site.register(AccountData)
admin.site.register(DesignData)
admin.site.register(AppointmentData)
admin.site.register(contactform)