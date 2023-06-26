from django.urls import path
from django.contrib.auth.views import LoginView,LogoutView
from apps_sinapsis.login_app.views import RegisterPage
from apps_sinapsis.login_app.views import LandingPage

urlpatterns = [
    path('', LandingPage.as_view( ), name='landing_page'),
    path('login/',LoginView.as_view(template_name = "login.html",extra_context={"title":"Login"}),name='login'),
    path('register/',RegisterPage.as_view(),name='register'),
    path('logout/',LogoutView.as_view(), name='logout')
]

