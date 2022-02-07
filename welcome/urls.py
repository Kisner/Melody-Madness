from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='welcome'),
    path("auth", views.auth_redir, name='auth'),
]