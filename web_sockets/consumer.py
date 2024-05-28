from channels.consumer import AsyncConsumer
import json
from channels.db import database_sync_to_async
from web_sockets.models import User


class EchoConsumer(AsyncConsumer):
    @database_sync_to_async
    def set_user_status(self, user):
        user_obj = User.objects.get(id=user['user_id'])
        user_obj.status = user['status']
        user_obj.save()

    async def websocket_connect(self, event):
        await self.send({
            "type": "websocket.accept",
        })

    async def websocket_receive(self, event):
        print("on message....")
        user_id = json.loads(event['text'])
        await self.set_user_status(user_id)
        await self.send({
            "type": "websocket.send",
            "text": json.dumps(user_id),
        })

    async def websocket_disconnect(self, event):
        print(">>>>>>>>>>>>>>>", event)
        print("disconnected...")


class UserStatus(AsyncConsumer):
    async def websocket_connect(self, event):
        await self.channel_layer.group_add(
            "user-status-notification",
            self.channel_name
        )
        await self.send({
            "type": "websocket.accept",
        })

    async def websocket_receive(self, event):
        print("on message....")
        print("************", event)
        await self.channel_layer.group_send(
            "user-status-notification",
            {
                "type": "noti.message",
                "message": event,
            }
        )

    async def noti_message(self, event):
        print("event..................", event)
        await self.send({"type": "websocket.send",  "text": json.dumps(event)})

    async def websocket_disconnect(self, event):
        await self.channel_layer.group_discard("user-status-notification", self.channel_name)
