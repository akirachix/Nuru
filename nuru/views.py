from multiprocessing import context
from os import confstr_names
from pyexpat.errors import messages
from re import template
from venv import create
from django.shortcuts import render
from dateutil.parser import parse
from .form import UserRegisrationForm, MessageRegisrationForm
import africastalking


# Create your views here.easy on me adele

import csv, io
from django.contrib.auth.decorators import permission_required

from nuru.models import Users

@permission_required('admin.can_add_log_entry')
def contact_upload(request):
    template="contact_upload.html"
    
    prompt={
        'order':'Order of the CSV should be first_name, last_name,Phone_number,child_name,child_date_of_birth,registration_date'
    }
    
    # GET request returns the value of the data with the specified key.

    if request.method== "GET":
        return render(request,template,prompt)
    
    csv_file=request.FILES['file']
    
     # let's check if it is a csv file

    if not csv_file.name.endswith('.csv'):
        messages.error(request,'This is not a csv file')
        
    data_set=csv_file.read().decode('UTF-8')
    
    # setup a stream which is when we loop through each line we are able to handle a data in a stream
  
    io_string=io.StringIO(data_set) 
    next(io_string)
    contact_upload= csv.reader(io_string,delimiter=',', quotechar="|")
    print(contact_upload)
    for full_name,Phone_number,child_name,child_date_of_birth, appointment_date,registration_date, *__ in contact_upload:
        dt = parse(child_date_of_birth)
        dts = parse(registration_date)
        created=Users( 
        full_name=full_name,
        child_name=child_name,
        child_date_of_birth=dt,
        registration_date=dts,
        phone_number=Phone_number,
        appointment_date = appointment_date,
        messages=messages

        )
        print(created)
        created.save()    
        
        context={}
        return render(request,template,context)

# UserRegisrationForm
    
def register_user(request):
    if request.method == "POST":
        form = UserRegisrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = UserRegisrationForm()
    return render(request,"registration/register_user.html",{"form":form})
    

def send_message(self):
    return("successfully sent")


# import self from
import africastalking
class SMS:
    def __init__(self):
        self.username = "nuru_care_infant_mortality"
        self.api_key = "8b1aad4aa0d3eaa3653db886c985afd5c7f41a96f30bbd4b595f5b715d97bb88"
        # Initialize the SDK
        africastalking.initialize(self.username, self.api_key)
        # Get the  SMS service
        self.sms = africastalking.SMS
    def send(self):
        recipients = ["+254112272857"]
        # +254723674180
        # Set your message
        message = "Hello Beryl, Welcome to NuruCare, Lulu will be receiving her 2nd dose of DPT on 23th November. #your child's health matters"
        # message = "Hello Linda Njeri, Welcome to NuruCare, Lulu will be receiving her 2nd dose of BCG on 12th November. To stop recieving these messages reply with STOP. #your child's health matters"
        # f
        # Set your shortCode or senderId
        # sender = "4632"
        try:
            response = self.sms.send(message, recipients)
            print (response)
        except Exception as e:
            print ('Encountered an error while sending: %s' % str(e))
if __name__ == '__main__':
     SMS().send()