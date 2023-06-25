from django import forms
from apps_sinapsis.custom_user.models import CustomUser

class CustomUserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = '__all__'
        
        # ['email',
        #         'password',
        #         'nombre',
        #         'apellido',
        #         ]
    