from typing import Any, Dict
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.list import ListView

from django.views.generic.edit import CreateView

from .models import Review
from apps_sinapsis.books.models import Book
from apps_sinapsis.sinapsis_cliente.mixins import OwnerSinapsisMixin
from django.contrib.auth.mixins import LoginRequiredMixin


from django.db.models import Q

from .forms import ReviewForm

# Create your views here.


class ReviewBaseList():
    template_name = "review.html"
    model = Review
    fields = '__all__'
    success_url = reverse_lazy('reviews:all')
    
class ReviewListView(ReviewBaseList,ListView):
    """
    List of reviews
    """
    
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context =  super().get_context_data(**kwargs)   
        return context
    
class ReviewQueriesList(ReviewBaseList,ListView):
    
    success_url = reverse_lazy('reviews:searcher')
    
    def get_context_data(self,**kwargs: Any) -> Dict[str, Any]:
        search_review = self.request.GET.get("search")
        context = super().get_context_data(**kwargs)
        context["filtered"] = Review.objects.filter(Q(book__nombre__icontains=search_review))
        return context
    
    
class ReviewCreateView(LoginRequiredMixin,OwnerSinapsisMixin,CreateView):
    
    template_name = "review_create.html"
    form_class = ReviewForm
    success_url = reverse_lazy('reviews:all')
    
    def form_valid(self,form):
        form.save()
        return super().form_valid(form)