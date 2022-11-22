from django.shortcuts import render
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
@csrf_exempt
def registration(request):
    if request.method == 'POST':
        session_id = request.POST.get('sessionId')
        short_code = request.POST.get('shortcode')
        phone_number = request.POST.get('Phone_number')
        text = request.POST.get('text')
        response=""
        if text == "":
            response = "CON Welcome to nuruCare \n"
            response += "Press 1 to opt-out \n"

    return HttpResponse({"NuruCare": "this method requires a POST "})


# import self from
# import africastalking
# class SMS:
#     def __init__(self):
#         self.username = "nuru_care_infant_mortality"
#         self.api_key = "8b1aad4aa0d3eaa3653db886c985afd5c7f41a96f30bbd4b595f5b715d97bb88"
#         # Initialize the SDK
#         africastalking.initialize(self.username, self.api_key)
#         # Get the  SMS service
#         self.sms = africastalking.SMS
#     def send(self):
#         recipients = ["+254112272857"]
#         # +254723674180
#         # Set your message
#         message = "Hello Beryl, Welcome to NuruCare, Lulu will be receiving her 2nd dose of DPT on 23th November. #your child's health matters"
#         # message = "Hello Linda Njeri, Welcome to NuruCare, Lulu will be receiving her 2nd dose of BCG on 12th November. To stop recieving these messages reply with STOP. #your child's health matters"
#         # f
#         # Set your shortCode or senderId
#         # sender = "4632"
#         try:
#             response = self.sms.send(message, recipients)
#             print (response)
#         except Exception as e:
#             print ('Encountered an error while sending: %s' % str(e))
# if __name__ == '__main__':
#      SMS().send()