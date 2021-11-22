from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Task, TimeEntry

class MainView(ListView):
    template_name = 'tasks/main.html'
    context_object_name = 'tasks_list'

    def get_taskset(self):
        """Return a list of the user's tasks."""
        return Task.objects

class TaskDetailView(DetailView):
    model = Task
    template_name = 'tasks/detail.html'

class TaskCreateView(CreateView):
    model = Task
    fields = ['name_text', 'desc_text', 'proj_text', 'status']

class TaskUpdateView(UpdateView):
    model = Task
    fields = ['name_text', 'desc_text', 'proj_text', 'status']

class TaskDeleteView(DeleteView):
    model = Task
    success_url = reverse_lazy('task-list')
