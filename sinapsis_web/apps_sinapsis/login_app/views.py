from django.views.generic.base import TemplateView


class LandingPage(TemplateView):
    template_name = 'landing_page.html'
    extra_context = {
        'title': 'SINAPSIS'
    }

class LoginPage(TemplateView):
    template_name='login.html'

class RegisterPage(TemplateView):
    template_name='register.html'