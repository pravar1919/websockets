from django.urls import path

from .views import chat, create_group_chat, create_one_to_one_chat

urlpatterns = [
    path('create/group/', create_group_chat, name='create_group_chat'),
    path('create/<int:user_id>/', create_one_to_one_chat,
         name='create_one_to_one_chat'),
    path("<str:group_name>/", chat),
]
