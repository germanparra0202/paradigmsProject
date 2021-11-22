from django.urls import path
from . import views

app_name = "tasks"

urlpatterns = [
    # Index View 
    path('',views.IndexView.as_view(), name='index'),   
    # Features 1-6
    path('<int:question_id>/tasks/', views.firstSixFeaturesQuestions.as_view(), name='features'),
    # Feature 7
    path('<int:question_id>/taskSeven/', views.QuestionSevenView.as_view(), name='featureSeven'),
    # Feature 8
    path('<int:question_id>/taskEight/', views.QuestionEightView.as_view(), name='featureEight'),
    # Results from features 
    path('<int:question_id>/results/', views.ResultsView.as_view(), name='results')  
]