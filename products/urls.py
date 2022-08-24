from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='web.products'),
    path('new', views.new)
]