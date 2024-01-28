from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("create_player", views.create_player, name="create-player"),
    path("create_day", views.create_day, name="create-day"),
]
