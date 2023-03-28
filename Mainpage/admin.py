from django.contrib import admin
from .models import AccountData,DesignData,AppointmentData,contactform,Temp_appointment

admin.site.register(AccountData)
admin.site.register(DesignData)
admin.site.register(AppointmentData)
admin.site.register(contactform)
admin.site.register(Temp_appointment)