from django.views.generic.base import TemplateView
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from apps_sinapsis.custom_user.forms import CustomUserForm

class LandingPage(TemplateView):
    template_name = 'landing_page.html'
    extra_context = {
        'title': 'SINAPSIS'
    }


class RegisterPage(CreateView):

    form_class = CustomUserForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
    extra_context = {
        'title': 'Register'
    }

    def form_valid(self, form):
        response = super().form_valid(form)
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password1')
        user = authenticate(email=email, password=password)
        login(self.request, user)
        return response
