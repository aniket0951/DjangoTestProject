from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('testfun/', TestFunc.as_view()),
    path('testme/', TestMe), 
]