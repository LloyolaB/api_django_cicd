from django.contrib import admin
from django.urls import path
from .views import indexLanding,hello_world
urlpatterns = [
    path('', indexLanding,name="landing"),
    path("holamundo",hello_world,name="holamundo")
]
