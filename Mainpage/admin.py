from django.contrib import admin
from .models import AccountData,DesignData,AppointmentData,contactform,Temp_appointment,PaymentData,TempPayment

class AccountDataAdmin(admin.ModelAdmin):
    list_display = ["email","acc_type","architech_fees"]

class DesignDataAdmin(admin.ModelAdmin):
    list_display = ["user_id","design_type","project_name","user_type"]

class AppointmentDataAdmin(admin.ModelAdmin):
    list_display = ["appointment_date","start_time","end_time","architech_id","user_id","architech_name","consumer_name","status"]

class PaymentDataAdmin(admin.ModelAdmin):
    list_display = ["appointment_id","user_id","architech_id","payment"]

admin.site.register(AccountData,AccountDataAdmin)
admin.site.register(DesignData,DesignDataAdmin)
admin.site.register(AppointmentData,AppointmentDataAdmin)
admin.site.register(contactform)
admin.site.register(Temp_appointment)
admin.site.register(PaymentData,PaymentDataAdmin)
admin.site.register(TempPayment)