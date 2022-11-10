from django import forms
from .models import Users
from .models import Message


class UserRegisrationForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = "__all__"

class MessageRegisrationForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = "__all__"        