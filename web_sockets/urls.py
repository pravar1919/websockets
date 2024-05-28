from django.urls import path

from .views import index, user_status, friend_request

urlpatterns = [
    path("", index),
    path("status/", user_status),
    path("friend-request/", friend_request),
]
