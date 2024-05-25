from django.shortcuts import render

from web_sockets.models import User

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
