from django import forms
from apps_sinapsis.custom_user.models import CustomUser

class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = [
            'username',
            'email',
            'password1',
            'password2'
        ]
