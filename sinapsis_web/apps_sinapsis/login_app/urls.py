from django.urls import path
from django.contrib.auth.views import LoginView ,LogoutView

from apps_sinapsis.login_app.views import LandingPage 
from apps_sinapsis.sinapsis_cliente.views import SignUpCliente

urlpatterns = [
    path('', LandingPage.as_view( ), name='landing_page'),
    path('login/',LoginView.as_view(template_name = "login.html"),name='login'),
    path('register/',SignUpCliente.as_view(),name='register'),
    path('logout/',LogoutView.as_view(), name='logout')
]

