from django.views.generic.base import TemplateView


class LandingPage(TemplateView):
    template_name = 'landing_page.html'
    extra_context = {
        'title': 'SINAPSIS'
    }

