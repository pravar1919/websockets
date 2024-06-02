from django.conf import settings
from django.db import models


class ChatGroup(models.Model):
    participants = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name='chat_groups')
    is_group = models.BooleanField(default=False)
    name = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name if self.is_group else f"Chat between {', '.join(user.username for user in self.participants.all())}"


class Message(models.Model):
    chat = models.ForeignKey(
        ChatGroup, related_name='messages', on_delete=models.CASCADE)
    sender = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='messages', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
