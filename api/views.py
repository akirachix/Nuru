from requests import Response
from rest_framework import viewsets
from .serializers import InformationSerializer, LoginSerializer,NotificationSerializer, RegisterSerializer, UsersSerializer
from nuru import models

from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView


class UsersViewSet(viewsets.ModelViewSet):
    queryset=models.Users.objects.all()
    serializer_class = UsersSerializer

class InformationViewSet(viewsets.ModelViewSet):
    queryset=models.Information.objects.all()
    serializer_class = InformationSerializer


class NotificationViewSet(viewsets.ModelViewSet):
    queryset=models.Notification.objects.all()
    serializer_class = NotificationSerializer


# class LoginView(APIView):
#     authentication_classes = (TokenAuthentication,)
#     permission_classes = (AllowAny,)
# def get(self,request,*args,**kwargs):
#     login = models.Register.objects.get(id=request.Register.id)
#     serializer = LoginSerializer(login)
#     return Response(serializer.data)

# class LoginView(generics.CreateAPIView):
#     queryset = models.Login.objects.all()
#     permission_classes = (AllowAny,)
#     serializer_class = LoginSerializer

class RegisterView(generics.CreateAPIView):
    queryset = models.Register.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer