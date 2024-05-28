from django.urls import path
from .consumer import UserChat

# Here, "" is routing to the URL EchoConsumer which
# will handle the chat functionality.
chat_urlpatterns = [
    path("ws/as/chat", UserChat.as_asgi()),
]
