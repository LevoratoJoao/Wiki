from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("search", views.search, name="search"),
    path("create", views.create, name="create"),
    path("randomPage", views.randomPage, name="randomPage"),
    path("edit/<str:pk>", views.edit, name="edit"),
    path("wiki/<str:pk>", views.entry, name="entry")
]
