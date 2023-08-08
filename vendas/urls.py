from django.urls import path

from .views import *

urlpatterns = [
    path('', vendas, name = 'vendas')
]