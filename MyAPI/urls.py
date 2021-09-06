from django.urls import path, include
from . import views
from rest_framework import routers
from .views import SearchResultsView

app_name = 'MyAPI'
urlpatterns = [
    path('', views.translated, name='home'),
    path('index/', views.index, name= 'index'),
    path('about/', views.about, name='about'),
    path('search/',SearchResultsView.as_view(), name='search_results'),
]