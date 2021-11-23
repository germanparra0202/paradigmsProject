from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Task

class MainView(ListView):
    model = Post
    template_name = 'tasks/main.html'
    context_object_name = 'main-view'

class TaskDetailView(DetailView):
    model = Task

class TaskCreateView(CreateView):
    model = Task
    fields = ['name_text', 'desc_text', 'proj_text', 'status']

class TaskUpdateView(UpdateView):
    model = Task
    fields = ['name_text', 'desc_text', 'proj_text', 'status']

class TaskDeleteView(DeleteView):
    model = Task
    success_url = '/'
