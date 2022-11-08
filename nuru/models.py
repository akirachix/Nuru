from django.db import models
from django.utils import timezone
# from phonenumber_field.formfields import PhoneNumberField


class Users(models.Model):
    full_name= models.CharField(max_length=20,null=True)
    Phone_number=models.CharField(max_length=15, null=True)
    child_name = models.CharField(max_length=30, null=True)
    child_date_of_birth = models.DateTimeField(default=timezone.now)
    registration_date = models.DateTimeField(default=timezone.now)
    appointment_date= models.DateTimeField(default=timezone.now)

    
class category(models.Model):
    neonatal_information=models.CharField(max_length=250, null=True)
    clinical_information=models.CharField(max_length=250, null=True)
    
class Information(models.Model):
    neonatal_information=models.CharField(max_length=250, null=True)
    clinical_information=models.CharField(max_length=250, null=True)

class Notification(models.Model):
    title=models.CharField(max_length=30, null=True)
    message = models.CharField(max_length=250, null=True)
    date_time = models.DateTimeField(default=timezone.now)


