from django.contrib import admin
from django.urls import path
from django.urls import include

from .views import ReviewListView

app_name = "reviews"

urlpatterns = [
    path("", ReviewListView.as_view(), name="all")
]