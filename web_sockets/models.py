from typing import Iterable
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
# Create your models here.


class User(AbstractUser):
    class Status(models.TextChoices):
        ONLINE = "online", _("Online")
        OFFLINE = "offline", _("Offline")

    status = models.CharField(
        max_length=20, choices=Status, default=Status.OFFLINE)

    def save(self, *args, **kwargs) -> None:
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "user-status-notification",
            {"type": "chat.message", "text": {
                "id": self.id, "status": self.status}},
        )
        return super(User, self).save(*args, **kwargs)


class Friends(models.Model):
    class Status(models.TextChoices):
        PENDING = "pending", _("Pending")
        ACCEPTED = "accepted", _("Accepted")
        REJECTED = "rejected", _("Rejected")

    user = models.ForeignKey(
        User, related_name="user_friends", on_delete=models.CASCADE)
    friend = models.ManyToManyField(User, blank=True, related_name="friends")
    status = models.CharField(
        max_length=20, choices=Status, default=Status.PENDING)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs) -> None:
        return super(Friends, self).save(*args, **kwargs)
