from rest_framework import viewsets
from .serializers import MotherSerializer,InformationSerializer,NotificationSerializer
from nuru import models

class MotherViewSet(viewsets.ModelViewSet):
    queryset=models.Mother.objects.all()
    serializer_class = MotherSerializer

class InformationViewSet(viewsets.ModelViewSet):
    queryset=models.Mother.objects.all()
    serializer_class = InformationSerializer

class NotificationViewSet(viewsets.ModelViewSet):
    queryset=models.Mother.objects.all()
    serializer_class = NotificationSerializer    
    