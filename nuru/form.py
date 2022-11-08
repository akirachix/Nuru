from django import forms
from .models import Users


class UserRegisrationForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = "__all__"