from django.contrib import admin
from django.urls import path
from django.urls import include

from .views import BooksListView

app_name = "books"

urlpatterns = [
    path("", BooksListView.as_view(), name="all")
]