from channels.consumer import AsyncConsumer
import json
from channels.db import database_sync_to_async

class UserChat(AsyncConsumer):
    async def websocket_connect(self, event):
        await self.channel_layer.group_add(
            "chat",
            self.channel_name
        )
        await self.send({
            "type": "websocket.accept",
        })

    async def websocket_receive(self, event):
        print("on message....")
        print("************", event)
        await self.channel_layer.group_send(
            "chat",
            {
                "type": "chat.message",
                "message": event,
            }
        )

    async def chat_message(self, event):
        print("event..................", event)
        await self.send({"type": "websocket.send",  "text": json.dumps(event)})

    async def websocket_disconnect(self, event):
        await self.channel_layer.group_discard("chat", self.channel_name)
