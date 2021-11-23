from django.urls import path
from . import views

app_name = "tasks"

urlpatterns = [
    # Main Window 
    path('', views.MainView.as_view(), name='main-view'),
    # Feature 1 --> Create
    path('tasks/add/', views.TaskCreateView.as_view(), name='task-add'),
    # Feature 2 --> Update
    path('tasks/<int:pk>/', views.TaskUpdateView.as_view(), name='task-update'),
    # Feature 3 --> Delete 
    path('tasks/<int:pk>/delete/', views.TaskDeleteView.as_view(), name='task-delete')
]
