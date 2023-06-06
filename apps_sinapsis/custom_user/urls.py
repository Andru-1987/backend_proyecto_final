from django.urls import path
from django.urls import include


from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView

urlpattersn = [
    path("login/",LoginView.as_view(template_name="custom_login.html"), name="login"),
    path("login/",LoginView.as_view(), name="logout")
]

