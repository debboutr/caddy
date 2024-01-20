from django.urls import path

from . import views

urlpatterns = [
    path("", views.GroupListView.as_view(), name="index"),
]
