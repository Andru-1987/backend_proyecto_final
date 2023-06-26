from django.contrib import admin
from django.urls import path
from django.urls import include

from .views import ReviewListView, ReviewQueriesList , ReviewCreateView

app_name = "reviews"

urlpatterns = [
    path("", ReviewListView.as_view(), name="all"),
    path("search",ReviewQueriesList.as_view(),name='searcher'),
    path("create/",ReviewCreateView.as_view(),name='create'),
]