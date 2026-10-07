from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("posts/create/", views.post_create, name="post_create"),
    path("posts/<slug:slug>/", views.post_detail, name="post_detail"),
    path("posts/<slug:slug>/edit/", views.post_edit, name="post_edit"),
]