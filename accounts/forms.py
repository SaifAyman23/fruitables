from django import forms
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']	    
        
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','username','email']
        
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields  = '__all__'        
        exclude = 'user',