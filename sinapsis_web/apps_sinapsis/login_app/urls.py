from django.urls import path
from apps_sinapsis.login_app.views import LandingPage,LoginPage,RegisterPage

urlpatterns = [
    path('', LandingPage.as_view( ), name='landing_page'),
    path('login/',LoginPage.as_view(),name='login'),
    path('register/',RegisterPage.as_view(),name='register'),
]

