from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='tournament'),
    path('vote_bracket/', views.vote_bracket, name='vote_bracket'),
]