from dataclasses import field
from rest_framework import serializers
from nuru.models import Mother,Notification,Information


class MotherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mother
        fields =('first_name','last_name','phone_number' ,'child_name','child_date_of_birth','registration_date')


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model =Notification
        field =('message','title','date_time')


class InformationSerializer(serializers.ModelSerializer):
    class Meta:
        model =Information
        field =('neonatal_information','clinical_information')




    
