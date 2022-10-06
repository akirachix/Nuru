from django.db import models

# Create your models here.

class Mother(models.Model):
    first_name= models.CharField(max_length=20 )
    last_name= models.CharField(max_length=20)
    phone_number= models.CharField(max_length=15)
    child_name = models.CharField(max_length=30)
    child_date_of_birth = models.DateField()
    registration_date = models.DateField()
 
class Information(models.Model):
    neonatal_information=models.CharField(max_length=250)
    clinical_information=models.CharField(max_length=250)

class Notification(models.Model):
    message = models.CharField(max_length=30)
    title = models.CharField(max_length=20)
    date_time = models.DateTimeField()
