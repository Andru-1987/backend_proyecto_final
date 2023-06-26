from django.shortcuts import render
from .forms import ClienteForm
from django.views.generic.edit import CreateView

# Create your views here.


class ClienteFormView(CreateView):
    form_class = ClienteForm
    
    def form_valid(self,form):
        form.save()
        return super().form_valid(form)