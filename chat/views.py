from django.shortcuts import render

# Create your views here.


def chat(request, group_name):
    context = {"name":group_name}
    return render(request, "chat/chat.html", context)
