from django.urls import path

from . import views

urlpatterns = [
    path("", views.episode_index, name="episode-index")
]