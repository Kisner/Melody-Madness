from django.urls import path
from . import views

urlpatterns = [
    path('', views.spauth, name='auth'),
    path('', views.spauth, name='data_index'),
    path("generate/", views.redir, name='generate'),
]