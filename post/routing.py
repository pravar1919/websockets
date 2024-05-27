from django.urls import path
from .consumer import PostLikeNotification


post_urlpatterns = [
    path("ws/as/post-like/", PostLikeNotification.as_asgi()),
]
