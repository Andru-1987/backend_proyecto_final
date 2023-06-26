from django.contrib import admin
from django.urls import path
from django.urls import include

from .views import BooksListView,BookDetailView ,BookCrearView,BookDeleteView,BookUpdateView


app_name = "books"

urlpatterns = [
    path("", BooksListView.as_view(), name="all"),
    path("<int:pk>/detail/",BookDetailView.as_view(), name="detail"),
    path("crear/",BookCrearView.as_view(), name="crear"),
    path("<int:pk>/update/",BookUpdateView.as_view(), name="update"),
    path("<int:pk>/delete/",BookDeleteView.as_view(), name="delete"),
] 