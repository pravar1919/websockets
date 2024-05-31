from web_sockets import routing
from post.routing import post_urlpatterns
from chat.routing import chat_urlpatterns
from channels.auth import AuthMiddlewareStack
import os
from django.urls import path
from channels.routing import ProtocolTypeRouter, URLRouter, ChannelNameRouter
from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    # Just HTTP for now. (We can add other protocols later.)
    "websocket": AuthMiddlewareStack(
        URLRouter(
            chat_urlpatterns + routing.websocket_urlpatterns +
            post_urlpatterns
        )
    )
})
