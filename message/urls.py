from django.urls import path

from message.apps import MessageConfig
from message.views import MessageCreateView, MessageListView

app_name = MessageConfig.name

urlpatterns = [
    path("message/", MessageListView.as_view(), name="message"),
    path("create_message", MessageCreateView.as_view(), name="create_message"),
]
