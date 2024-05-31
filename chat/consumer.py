from channels.consumer import AsyncConsumer
from channels.exceptions import StopConsumer
import json


class UserChat(AsyncConsumer):
    async def websocket_connect(self, event):
        print(self.scope['url_route']['kwargs']['name'])
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
        await self.send({"type": "websocket.send",  "text": event['message']['text']})

    async def websocket_disconnect(self, event):
        await self.channel_layer.group_discard("chat", self.channel_name)
        # raise StopConsumer()
