from django.urls import path

from .views import *

urlpatterns = [
    path('', authorization, name = 'authorization')
]