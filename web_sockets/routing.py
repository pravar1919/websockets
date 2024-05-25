from django.urls import path
from .consumer import EchoConsumer, UserStatus

# Here, "" is routing to the URL EchoConsumer which
# will handle the chat functionality.
websocket_urlpatterns = [
    path("ws/as/", EchoConsumer.as_asgi()),
    path("ws/as/status", UserStatus.as_asgi()),
]
