from django.shortcuts import render

# Create your views here.


def chat(request):
    context = {"name":"my-group"}
    return render(request, "chat/chat.html", context)
