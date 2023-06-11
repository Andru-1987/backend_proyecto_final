from django.views.generic.base import TemplateView
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


class LandingPage(TemplateView):
    template_name = 'landing_page.html'
    extra_context = {
        'title': 'SINAPSIS'
    }

class LoginPage(TemplateView):
    template_name='login.html'

class RegisterPage(TemplateView):
    template_name='register.html'
    
    
    

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return response