from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='products'),
    path('details/<int:id>', views.details, name='productDetails')
]