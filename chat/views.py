from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

from chat.models import ChatGroup, Message
# from web_sockets.models import User
# Create your views here.

User = get_user_model()


def chat(request, group_name):
    user_qs = User.objects.all().exclude(id=request.user.id)
    chat_id = create_one_to_one_chat(request, user_qs.first().id)
    chats_qs = Message.objects.filter(chat_id=chat_id).order_by("timestamp")
    context = {"name": group_name, "user_qs": user_qs,
               "chat_id": chat_id, "chats": chats_qs}
    return render(request, "chat/chat.html", context)


@login_required
def create_one_to_one_chat(request, user_id):
    user = get_object_or_404(User, id=user_id)
    chat, created = ChatGroup.objects.get_or_create(is_group=False)
    chat.participants.add(request.user, user)
    chat.name = f"{request.user.username}-{user.username}"
    chat.save()
    return chat.id
    return JsonResponse({'chat_id': chat.id})


@login_required
def create_group_chat(request):
    if request.method == "POST":
        name = request.POST.get('name')
        participants = request.POST.getlist('participants')
        chat = ChatGroup.objects.create(name=name, is_group=True)
        chat.participants.add(*participants)
        chat.participants.add(request.user)
        return JsonResponse({'chat_id': chat.id})
    users = User.objects.exclude(id=request.user.id)
    return render(request, 'chat/create_group_chat.html', {'users': users})
