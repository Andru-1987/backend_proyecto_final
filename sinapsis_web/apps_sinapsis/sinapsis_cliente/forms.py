from django import forms
from .models import SinapsisUser

from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):

    
    class Meta:
        model = SinapsisUser
        fields = [
            "email",
            "password",
            "is_sinapsis_owner" ,
            "is_sinapsis_manager" , 
            "is_sinapsis_user" ,
        ]
        
        widgets = {
            
            'password': forms.PasswordInput() 
        }
   