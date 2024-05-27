from django.db import models
from django.conf import settings

# Create your models here.


class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             related_name="posts", on_delete=models.CASCADE)
    message = models.TextField()
    like = models.ManyToManyField(
        settings.AUTH_USER_MODEL, through="LikedPost")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    @property
    def get_likes(self):
        if self.like.all().exists():
            return self.like.all().count() - 1
        return 0

    @property
    def are_likes(self):
        if self.like.all().exists():
            return True
        return False

    @property
    def get_last_liked_name(self):
        if self.like.all().exists():
            return self.like.all().first().username


class LikedPost(models.Model):
    post = models.ForeignKey(
        Post, related_name="liked_posts", on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             related_name="liked_posts", on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
