from django.urls import path
from clientside import views

urlpatterns = [
    path('', views.home)
]