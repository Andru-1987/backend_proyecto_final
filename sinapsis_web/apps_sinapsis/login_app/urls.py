from django.urls import path
from django.contrib.auth.views import LoginView

from apps_sinapsis.login_app.views import LandingPage,RegisterPage

urlpatterns = [
    path('', LandingPage.as_view( ), name='landing_page'),
    path('login/',LoginView.as_view(),name='login'),
    path('register/',RegisterPage.as_view(),name='register'),
]

