from rest_framework import viewsets
from .serializers import InformationSerializer,NotificationSerializer, UsersSerializer,MessageSerializer,Contact_numberSerializer
from nuru import models
import africastalking
class UsersViewSet(viewsets.ModelViewSet):
    queryset=models.Users.objects.all()
    serializer_class = UsersSerializer

class InformationViewSet(viewsets.ModelViewSet):
    queryset=models.Information.objects.all()
    serializer_class = InformationSerializer


class NotificationViewSet(viewsets.ModelViewSet):
    queryset=models.Notification.objects.all()
    serializer_class = NotificationSerializer


class MessageViewSet(viewsets.ModelViewSet):
    queryset=models.Message.objects.all()
    serializer_class = MessageSerializer


class Contact_numberViewSet(viewsets.ModelViewSet):
    queryset=models.Contact_number.objects.all()
    serializer_class=Contact_numberSerializer
    


class SMS:
    def __init__(self):
                self.username = "nurusms"
                self.api_key = "cdb2accc90a1c54c800a5a64f2ee46f0e58129d076237aaafc6ab5a90891e749"
            # Initialize the SDK
                africastalking.initialize(self.username, self.api_key)
            # Get the  SMS service
                self.sms = africastalking.SMS
    def send(self):
            recipients = models.Users.full_name
            message =(f"Hello {recipients.full_name} Welcome to NuruCare, {recipients.child_name} will be receiving her 2nd dose of BCG on {recipients.appointment_date}. #your child's health matters")
            try:
                response = self.sms.send(message, models.Users)
                print (response)
            except Exception as e:
                print ('Encountered an error while sending: %s' % str(e))
                if __name__ == '__main__':
                 SMS().send()  