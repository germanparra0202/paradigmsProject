from django.urls import path
from . import views

app_name = "tasks"

urlpatterns = [
    # First list view, main view 
    path('index/', views.index, name='main-view'),
    # Feature 1
    path('featureone/', views.featureOne.as_view(), name='feature'),   
    # Features 2-6
    path('features/', views.feature2through6.as_view(), name='featurestwothroughsix'),
    # Feature 7
    path('featureseven/', views.featureSevenView.as_view(), name='featureSeven'),
    # Feature 8
    path('featureeight/', views.featureEightView.as_view(), name='featureEight') 
]
