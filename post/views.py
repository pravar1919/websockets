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


def post_detail(request):
    context = {}
    return render(request, "post/post-detail.html", context)


def add_remove_like(request):
    data = json.loads(request.body)
    obj, created = LikedPost.objects.get_or_create(
        post_id=data["post_id"], user=request.user)
    if not created:
        obj.delete()
        post_obj = Post.objects.get(id=data["post_id"])
        context = {
            "are_likes": post_obj.are_likes,
            "get_last_liked_name": post_obj.get_last_liked_name,
            "get_likes": post_obj.get_likes
        }
        return JsonResponse({"message": "Like removed", **context})

    return JsonResponse({"message": "Liked",
                         "are_likes": obj.post.are_likes,
                         "get_last_liked_name": obj.post.get_last_liked_name,
                         "get_likes": obj.post.get_likes
                         })
