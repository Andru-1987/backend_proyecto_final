from django.contrib import admin
from django.urls import path
from django.urls import include

from .views import StoreListView,StoreDetailView ,StoreCreateView ,StoreDeleteView , StoreUpdateView


app_name = "stores"

urlpatterns = [
    path("", StoreListView.as_view(), name="all"),
    path("<int:pk>/detail/",StoreDetailView.as_view(), name="detail"),
    path("<int:pk>/borrar/",StoreDeleteView.as_view(), name="borrar"),
    path("<int:pk>/update/",StoreUpdateView.as_view(), name="update"),
    path("crear/", StoreCreateView.as_view(), name="crear"),
    
    
] 