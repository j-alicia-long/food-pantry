from django.urls import path

from . import views

app_name = 'fridge_app' 

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('food/', views.LogFoodView.as_view(), name='food')
]
