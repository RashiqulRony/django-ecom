from django.urls import path
from . import views


urlpatterns = [
    path('', views.login, name='web.login'),
    path('login', views.login, name='web.login'),
    path('register', views.register, name='web.register'),
]