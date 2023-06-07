from django.contrib import admin
from django.urls import path
from django.urls import include

urlpatterns = [
    path("/", include("apps_sinapsis.login_app.urls")),
    path("admin/", admin.site.urls),
    path("usuarios/", include("apps_sinapsis.custom_user.urls"))
]
