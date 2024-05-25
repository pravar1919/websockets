from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
# Create your models here.


class User(AbstractUser):
    class Status(models.TextChoices):
        ONLINE = "online", _("Online")
        OFFLINE = "offline", _("Offline")

    status = models.CharField(
        max_length=20, choices=Status, default=Status.OFFLINE)
