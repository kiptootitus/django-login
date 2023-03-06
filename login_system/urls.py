from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('welcome', views.welcome, name='welcome'),
    # path('register/', views.register, name='register'),
]