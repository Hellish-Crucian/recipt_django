from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView 
# Create your views here.
from core import models


class List(ListView):
    template_name = 'core/list.html'
    context_object_name = 'ctx'
    model = models.Recipt
    
class ResiptDetailView(DetailView):
    model = models.Recipt
    template_name = 'core/detale.html'
    context_object_name = 'ctx'