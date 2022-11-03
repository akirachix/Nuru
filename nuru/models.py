from django.db import models
# from phonenumber_field.formfields import PhoneNumberField


class Users(models.Model):
    full_name= models.CharField(max_length=20)
    Phone_number=models.CharField(max_length=15)
    child_name = models.CharField(max_length=30)
    child_date_of_birth = models.DateField()
    registration_date = models.DateField()
    appointment_dates = models.DateField()

    
class category(models.Model):
    neonatal_information=models.CharField(max_length=250)
    clinical_information=models.CharField(max_length=250)
    
class Information(models.Model):
    neonatal_information=models.CharField(max_length=250)
    clinical_information=models.CharField(max_length=250)

class Notification(models.Model):
    title=models.CharField(max_length=30)
    message = models.CharField(max_length=200)
    date_time = models.DateTimeField(null=True)

