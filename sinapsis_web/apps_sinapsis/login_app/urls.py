from django.urls import path
from apps_sinapsis.login_app.views import Login

urlpatterns = [
    path('', Login.as_view( ), name='landing_page'),
]

