from django.urls import path
from .views import *




from django.urls import path
from . import views

urlpatterns = [
    path('about/<int:pk>/', views.about_detail, name='about_detail'),
]


