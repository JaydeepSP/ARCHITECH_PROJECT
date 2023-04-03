from django.db import models
import datetime


class AccountData(models.Model):
    acc_id = models.IntegerField(default=0)
    email = models.EmailField(max_length=100,default="")
    acc_type = models.TextField(max_length=100,default="")
    architech_fees = models.IntegerField(default=0)

    def __str__(self):
        return str(self.acc_id) + " - " + self.acc_type
    
class DesignData(models.Model):
    design_id = models.AutoField
    user_id = models.IntegerField(default=0)
    design_img = models.ImageField(upload_to="design_img/")
    design_type = models.TextField(max_length=50,default="")
    project_name = models.TextField(max_length=200,default="")
    design_desc = models.TextField(max_length=5000,default="")
    user_type = models.TextField(max_length=50,default="")

    def __str__(self):
        return str(self.user_id) + " - " + self.design_type
    
class AppointmentData(models.Model):
    appointment_id = models.AutoField
    appointment_date = models.DateField(default=datetime.date.today)
    start_time = models.TextField(max_length=50,default="")
    end_time = models.TextField(max_length=50,default="")
    appointment_desc = models.TextField(max_length=500,default="")
    architech_id = models.IntegerField(default=0)
    user_id = models.IntegerField(default=0)
    architech_name = models.TextField(max_length=100,default="")
    consumer_name = models.TextField(max_length=150,default="")
    status = models.TextField(max_length=40,default="In Waiting")

    def __str__(self):
        return str(self.architech_id) + " - " + str(self.user_id)
    
class contactform(models.Model):
    contact_id = models.AutoField
    email_id = models.EmailField(max_length=100,default="")
    message = models.TextField(max_length=500,default="")

    def __str__(self):
        return self.email_id
    
class Temp_appointment(models.Model):
    user_id = models.IntegerField(default=0)
    appointment_date = models.DateField(default=datetime.date.today)
    start_time = models.TextField(max_length=50,default="")
    end_time = models.TextField(max_length=50,default="")
    appointment_desc = models.TextField(max_length=500,default="")
    architech_id = models.IntegerField(default=0)


class PaymentData(models.Model):
    payment_id = models.AutoField
    appointment_id = models.IntegerField(default=0)
    user_id = models.IntegerField(default=0)
    architech_id = models.IntegerField(default=0)
    payment = models.IntegerField(default=0)

class TempPayment(models.Model):
    amount = models.IntegerField(default=0)
    app_id = models.IntegerField(default=0)
    architech_id = models.IntegerField(default=0)