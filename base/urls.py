from django.urls import path
from . import views
from django.urls import include

urlpatterns = [
    path('', views.home_page, name='homepage'),
    path('dashboard', views.home_page, name='homepage'),
    path('signup', views.sign_up, name='singup'),
    path('login', views.home_page, name='homepage')
]