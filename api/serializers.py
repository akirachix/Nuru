from dataclasses import field, fields
from pyexpat import model
from rest_framework import serializers
from nuru.models import Mother,Information, Notification


class MotherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mother
        fields =('first_name','last_name','phone_number' ,'child_name','child_date_of_birth','registration_date')

class InformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Information
        fields =('neonatal_information','clinical_information')


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Notification
        fields=('title','message','date_time')


    
