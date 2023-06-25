from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from .models import Review

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