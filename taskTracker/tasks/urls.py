from django.urls import path
from . import views

app_name = "tasks"

urlpatterns = [
    # Main Window 
    path('task/', views.MainView.as_view(), name='main-view'),
    # Feature 1 --> Create
    path('task/add/', views.TaskCreateView.as_view(), name='task-add'),
    # Feature 2 --> Update
    path('task/<int:pk>/', views.TaskUpdateView.as_view(), name='task-update'),
    # Feature 3 --> Delete 
    path('task/<int:pk>/delete/', views.TaskDeleteView.as_view(), name='task-delete')
]
