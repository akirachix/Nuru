
from rest_framework import serializers
from nuru.models import Information, Notification, Users,Message


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
        fields=('Title','message','date_time')


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model=Message
        fields=('Phone_number','date_time','message',)





    
