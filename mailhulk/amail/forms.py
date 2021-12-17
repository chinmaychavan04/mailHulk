from django import forms
from django.db.models import fields
from .models import Mail

class Mailform(forms.ModelForm):
    class Meta:
        model = Mail
        fields = ['event','email']