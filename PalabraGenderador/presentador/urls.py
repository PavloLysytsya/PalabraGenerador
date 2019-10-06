from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('new/', views.post_new, name='post_new'),
    path('present/', views.presentation, name='presentation'),
]
