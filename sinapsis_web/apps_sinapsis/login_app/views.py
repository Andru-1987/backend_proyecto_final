from django.views.generic.base import TemplateView


class Login(TemplateView):
    template_name = 'login.html'
    extra_context = {
        'title': 'LOGIN SINAPSIS'
    }
