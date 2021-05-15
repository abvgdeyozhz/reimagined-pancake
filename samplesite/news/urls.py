from django.contrib import admin
from django.urls import path, include

from news.views import *

urlpatterns = [
   path('', index),
    path('test/', test),
]
