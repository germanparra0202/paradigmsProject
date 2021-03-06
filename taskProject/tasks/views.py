from django.shortcuts import render
from .models import Task
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.
class IndexView(ListView):
    model = Task
    template_name = 'tasks/index.html'
    context_object_name = 'index'

class SingleView(DetailView):
    model = Task
    pk_url_kwarg = 'pk'
    template_name = 'tasks/single.html'
    context_object_name = 'task'

class TasksView(ListView):
    model = Task
    template_name = 'tasks/tasks.html'
    context_object_name = 'task_list'

class AddView(CreateView):
    model = Task
    template_name = 'tasks/add.html'
    fields = '__all__'
    success_url = reverse_lazy('tasks:tasks')

class EditView(UpdateView):
    model = Task
    template_name = 'tasks/edit.html'
    fields = '__all__'
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('tasks:tasks')
    

class Delete(DeleteView):
    model = Task
    template_name = 'tasks/confirm-delete.html'
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('tasks:tasks')
