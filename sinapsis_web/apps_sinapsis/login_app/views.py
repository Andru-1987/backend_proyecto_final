from django.views.generic.base import TemplateView
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from apps_sinapsis.custom_user.forms import CustomUserForm


from apps_sinapsis.cliente.forms import ClienteForm

class LandingPage(TemplateView):
    template_name = 'landing_page.html'
    extra_context = {
        'title': 'SINAPSIS'
    }


class RegisterPage(CreateView):

    form_class = ClienteForm
    success_url = reverse_lazy('reviews:all')
    template_name = 'signup.html'
    extra_context = {
        'title': 'Register'
    }

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
