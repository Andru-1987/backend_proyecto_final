from typing import Any, Dict
from django.shortcuts import render

from django.urls import reverse_lazy
from .models import Book , GENERO
from .models import Store

from django.views.generic.list import ListView


# Create your views here.
class BooksBaseView():
    template_name = 'book_list.html'
    model = Book
    fields = '__all__'
    sucess_url = reverse_lazy('books:all')
    
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        return context
    

class BooksListView(BooksBaseView,ListView):
    """
    Lista de Books
    """