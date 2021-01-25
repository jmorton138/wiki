from django.urls import path, include

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("q=", views.search, name="search"),
    path("<str:title>/", views.entry, name="entry"),
    path("new_page", views.add, name="add"),
    path("<str:title>/edit", views.edit, name="edit")
]
