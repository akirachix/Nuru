from rest_framework import viewsets
from .serializers import InformationSerializer,NotificationSerializer, UsersSerializer,MessageSerializer,Contact_numberSerializer
from nuru import models

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
    


