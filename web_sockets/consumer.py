from channels.consumer import AsyncConsumer
import json
from channels.db import database_sync_to_async
from web_sockets.models import User
from django.core import serializers


class EchoConsumer(AsyncConsumer):
    @database_sync_to_async
    def set_user_status(self, user):
        print("**********", user)
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
    @database_sync_to_async
    def get_user_status(self):
        print(">>>>>>>>>>>>>>>", )
        return serializers.serialize('json',
                                     User.objects.all())

    async def websocket_connect(self, event):
        await self.send({
            "type": "websocket.accept",
        })

    async def websocket_receive(self, event):
        print("on message....")
        # user_id = json.loads(event['text'])
        users = await self.get_user_status()
        print("************", users)
        await self.send({
            "type": "websocket.send",
            "text": users,
        })

    async def websocket_disconnect(self, event):
        pass
