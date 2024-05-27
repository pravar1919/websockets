import json
from django.http import JsonResponse
from django.shortcuts import render
from .models import LikedPost, Post
# Create your views here.


def home(request):
    post_qs = Post.objects.all()
    context = {
        "obj": post_qs,
    }
    return render(request, "post/home.html", context)


def add_remove_like(request):
    data = json.loads(request.body)
    obj, created = LikedPost.objects.get_or_create(
        post_id=data["post_id"], user=request.user)
    print(obj)
    if not created:
        obj.delete()
        return JsonResponse({"message": "Like removed"})
    return JsonResponse({"message": "Liked"})
