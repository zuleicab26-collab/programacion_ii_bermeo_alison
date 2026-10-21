from django.urls import path
from . import views

app_name = "tasks"

urlpatterns = [
    path("", views.home, name="home"),
    path("register/", views.register, name="register"),
    path("about_me/", views.about_me, name="about_me"),
]