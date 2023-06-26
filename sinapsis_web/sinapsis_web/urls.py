from django.contrib import admin
from django.urls import path
from django.urls import include

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("", include("apps_sinapsis.login_app.urls")),
    path("admin/", admin.site.urls),
    path("usuarios/", include("apps_sinapsis.custom_user.urls")),
    path("books/",include("apps_sinapsis.books.urls")),
    path("blog/",include("apps_sinapsis.reviews.urls")),
    path("contact/", include("apps_sinapsis.books.store_urls")),
]

urlpatterns += static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT )