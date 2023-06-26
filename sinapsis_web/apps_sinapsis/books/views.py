from typing import Any, Dict
from django.shortcuts import render

from django.urls import reverse_lazy , reverse
from .models import Book , GENERO
from .models import Store

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from django.views.generic.edit import DeleteView , CreateView , UpdateView 


from apps_sinapsis.sinapsis_cliente.mixins import OwnerSinapsisMixin
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class BooksBaseView():
    template_name = 'book_list.html'
    model = Book
    fields = '__all__'
    sucess_url = reverse_lazy('books:all')
    
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        return context
    

class BooksListView(LoginRequiredMixin,BooksBaseView,ListView):
    """
    Lista de Books
    """
    
class BookDetailView(LoginRequiredMixin,BooksBaseView,DetailView):
    template_name = "blog_detail.html"
    
class BookCrearView(LoginRequiredMixin,OwnerSinapsisMixin,BooksBaseView,CreateView):
    template_name = "book_create.html"
    extra_context = {
        "tipo" : "Agregar"
    }
    
    def get_success_url(self) -> str:
        return reverse('books:all')
    
class BookUpdateView(LoginRequiredMixin,OwnerSinapsisMixin,BooksBaseView,UpdateView):
    template_name = "book_create.html"
    
    extra_context = {
        "tipo" : "Modificar"
    }
    
    def get_success_url(self) -> str:
        return reverse('books:all')
    
class BookDeleteView(LoginRequiredMixin,OwnerSinapsisMixin,BooksBaseView,DeleteView):
    
    def get_success_url(self) -> str:
        return reverse('books:all')
    
    
    
    
    

class StoreBaseView():
    template_name = 'contact_list.html'
    model = Store
    fields = '__all__'
    sucess_url = reverse_lazy('stores:all')
    
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        return context

class StoreListView(LoginRequiredMixin,StoreBaseView,ListView):
    """
    Lista de Stores
    """
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["filtered"] = Store.objects.all().values()
        return context
    
    
class StoreDetailView(LoginRequiredMixin,StoreBaseView,DetailView):
    template_name = "contact_detail.html"
    
    
class StoreCreateView(LoginRequiredMixin,OwnerSinapsisMixin,StoreBaseView,CreateView):
    template_name = "store_create.html"
    extra_context = {
        "tipo" : "Agregar"
    }
    
    def get_success_url(self) -> str:
        return reverse('stores:all')
    
    
    
class StoreUpdateView(LoginRequiredMixin,OwnerSinapsisMixin,StoreBaseView,UpdateView):
    template_name = "store_create.html"
    extra_context = {
        "tipo" : "Modificar"
    }
    
    def get_success_url(self) -> str:
        return reverse('stores:all')
    
class StoreDeleteView(LoginRequiredMixin,OwnerSinapsisMixin,StoreBaseView,DeleteView):    
    def get_success_url(self) -> str:
        return reverse('stores:all')