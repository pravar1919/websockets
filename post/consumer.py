from channels.consumer import AsyncConsumer
import json
from channels.exceptions import StopConsumer
from channels.db import database_sync_to_async
from web_sockets.models import User


class PostLikeNotification(AsyncConsumer):
    async def websocket_connect(self, event):
        await self.channel_layer.group_add(
            "user-like-post-notification",
            self.channel_name
        )
        await self.send({
            "type": "websocket.accept",
        })

    async def websocket_receive(self, event):
        print("on message....")
        print("************", event)
        await self.channel_layer.group_send(
            "user-like-post-notification",
            {
                "type": "like.message",
                "message": event,
            }
        )

    async def like_message(self, event):
        print("event..................", event)
        await self.send({"type": "websocket.send",  "text": json.dumps(event)})

    async def websocket_disconnect(self, event):
        await self.channel_layer.group_discard("user-like-post-notification", self.channel_name)
        raise StopConsumer()
