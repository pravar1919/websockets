from django.urls import path

from .views import index, user_status

urlpatterns = [
    path("", index),
    path("status/", user_status),
]
