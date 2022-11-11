from django import forms
from .models import Users
from .models import Message
from .models import Contact_number


class UserRegisrationForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = "__all__"

class MessageRegisrationForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = "__all__"


class Contact_numberRegisrationForm(forms.ModelForm):
    class Meta:
        model = Contact_number
        fields = "__all__"


                           