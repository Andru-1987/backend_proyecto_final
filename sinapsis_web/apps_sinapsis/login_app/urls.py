from django.urls import path
from django.urls import include

from apps_sinapsis.login_app.views import LoginTemplate


urlpatterns = [
    path('', LoginTemplate.as_view(), name='landing_page')
]

