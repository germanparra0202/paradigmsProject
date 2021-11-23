from django.urls import path
from . import views

app_name = 'tasks'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>', views.SingleView.as_view(), name='single')
]