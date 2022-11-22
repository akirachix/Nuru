
from rest_framework import serializers
from nuru.models import Information, Notification, Users,Message,Contact_number


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields =('full_name','Phone_number' ,'child_name','child_date_of_birth','registration_date','appointment_date')

class InformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Information
        fields =('neonatal_information','clinical_information')


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Notification
        fields=('title','message','date_time')


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model=Message
        fields=('full_name','child_name','appointment_date')

class Contact_numberSerializer(serializers.ModelSerializer):
    class Meta:
        model=Contact_number
        fields=('Phone_number','name')        




    
