from django.urls import path
from . import views

app_name = "tasks"

urlpatterns = [
    # Main Window 
    path('', MainView.as_view(), name='main-view'),
    # Detail View
    path('<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    # Feature 1 --> Create
    path('add/', TaskCreateView.as_view(), name='task-add'),
    # Feature 2 --> Update
    path('<int:pk>/update/', views.TaskUpdateView.as_view(), name='task-update'),
    # Feature 3 --> Delete 
    path('<int:pk>/delete/', views.TaskDeleteView.as_view(), name='task-delete')
]
