from django.urls import path
from . import views
from django.urls import include

urlpatterns = [
    path('', views.users_page, name='userspage'),
    path('dashboard', views.users_page, name='userspage'),
    path('signup', views.sign_up, name='singup'),
    path('login', views.home_page, name='homepage')
]