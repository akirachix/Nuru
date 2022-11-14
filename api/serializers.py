from codecs import register
from dataclasses import field, fields
from operator import mod
from pyexpat import model
from rest_framework import serializers
from nuru.models import Information, Login,  Notification, Users,Register
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password





class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields =('full_name','phone_number' ,'child_name','child_date_of_birth','registration_date','appointment_date')

class InformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Information
        fields =('neonatal_information','clinical_information')


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Notification
        fields=('title','message','date_time')

# class LoginSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=Register
#         fields=('username','password',)

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model=Register
        fields=('first_name','last_name','phone_number','password','password2',)
           
def validate(self,attrs):
     if attrs['password'] != attrs['password2']:
                raise serializers.ValidationError({"password": "Password fields didn't match."})
     return attrs
    
def create(self, validated_data):
            user = Register.objects.create(
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            phone_number=validated_data['phone_number'],
            password=validated_data['password'],
            password2=validated_data['password2'],
        )
        
            user.set_password(validated_data['password'])
            user.save()

            return user
        
