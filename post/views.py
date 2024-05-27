from django.shortcuts import render
from .models import Post
# Create your views here.


def home(request):
    post_qs = Post.objects.all()
    context = {
        "obj": post_qs
    }
    return render(request, "post/home.html", context)

