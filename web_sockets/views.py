from django.http import JsonResponse
from django.shortcuts import render

from web_sockets.models import Friends, User

# Create your views here.


def index(request):
    context = {}
    return render(request, 'index.html', context)


def user_status(request):
    user_obj = User.objects.all()
    context = {
        "obj": user_obj
    }
    return render(request, 'user_status.html', context)


def friend_request(request):
    friend_obj, created = Friends.objects.get_or_create(user_id=1)
    friend_obj.friend.add(User.objects.get(id=3))
    friend_obj.save()
    return JsonResponse("created", safe=False)
