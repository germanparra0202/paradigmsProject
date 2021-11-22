"""taskTracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from . import views

app_name = "tasks"

urlpatterns = [
    # Index View 
    path('',views.IndexView.as_view(), name='index'),   
    # Features 1-6
    #path('<int:question_id>/tasks/', views.firstSixFeaturesQuestions.as_view(), name='features'),
    # Feature 7
    path('<int:question_id>/taskSeven/', views.QuestionSevenView.as_view(), name='featureSeven'),
    # Feature 8
    path('<int:question_id>/taskEight/', views.QuestionEightView.as_view(), name='featureEight'),
    # Results from features 
    path('<int:question_id>/results/', views.ResultsView.as_view(), name='results')  
]
