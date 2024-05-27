from django.urls import path

from .views import home, add_remove_like, post_detail

urlpatterns = [
    path("", home),
    path("post-detail/", post_detail, name="post_detail"),
    path("like/", add_remove_like, name="like"),
]
