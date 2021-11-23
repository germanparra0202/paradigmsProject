from django.urls import path
from . import views

app_name = 'tasks'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('add/', views.AddView.as_view(), name='add'),
    path('tasks/', views.TasksView.as_view(), name='tasks'),
    path('<int:pk>/', views.SingleView.as_view(), name='single')

]