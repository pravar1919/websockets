from django.urls import path

from .views import home, add_remove_like

urlpatterns = [
    path("", home),
    path("like/", add_remove_like, name="like"),
]
