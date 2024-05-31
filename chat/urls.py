from django.urls import path

from .views import chat

urlpatterns = [
    path("<str:group_name>/", chat)
]
