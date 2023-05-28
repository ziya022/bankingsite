from django.urls import path
from bankapp import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('appli', views.appli, name='appli'),
    path('logout', views.logout, name='logout'),
]
