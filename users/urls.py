from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('', views.login, name='login'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.user_logout, name='logout'),

    # dashboard
    path('dashboard', views.dashboard, name='dashboard'),
]