from django.shortcuts import render
from .models import Core
from django.views.generic import ListView, DetailView, UpdateView

# Create your views here.
class IndexView(ListView):
    model = Task
    template_name = 'tasks/index.html'
    context_object_name = 'index'

class SingleView(DetailView):
    model = Task
    template_name = 'tasks/single.html'
    context_object_name = 'task'