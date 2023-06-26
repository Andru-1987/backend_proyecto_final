
from django.views.generic import CreateView
from django.urls import reverse_lazy

from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm

class SignUpCliente(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    