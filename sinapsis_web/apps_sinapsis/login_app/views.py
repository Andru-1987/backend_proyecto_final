from django.shortcuts import render
from django.views.generic import TemplateView


class LoginTemplate(TemplateView):
    template_name = 'login.html'
    context = {
        'title': 'LOGIN SINAPSIS'
    }

