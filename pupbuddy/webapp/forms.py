from django import forms

from django.contrib.auth.models import User
from webapp.models import *

class RegistrationForm(forms.Form):
    username = forms.CharField(max_length = 20,
                               widget = forms.TextInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(max_length = 200, 
                                label='Password', 
                                widget = forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(max_length = 200, 
                                label='Confirm password',  
                                widget = forms.PasswordInput(attrs={'class':'form-control'}))
    deviceNumber = forms.IntegerField(min_value=0, 
                                      max_value=999999999999,
                                      widget = forms.TextInput(attrs={'class':'form-control'}))
    
    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords did not match.")
        return cleaned_data

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username__exact=username):
            raise forms.ValidationError("Username is already taken.")
        return username
    
    def clean_devicenumber(self):
        deviceNumber = self.cleaned_data.get('deviceNumber')
        if Profile.objects.filter(deviceNumber__exact=deviceNumber):
            raise forms.ValidationError("Device number is already registered.")
        return deviceNumber
