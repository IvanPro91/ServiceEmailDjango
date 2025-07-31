from django.urls import path

from mailing.apps import MailingConfig
from mailing.views import MailingListView, MailingCreateView, MessageCreateView, MessageListView

app_name = MailingConfig.name

urlpatterns = [
    path("", MailingListView.as_view(), name="mailing"),
    path("message/", MessageListView.as_view(), name="message"),
    path("create_mailing", MailingCreateView.as_view(), name="create_mailing"),
    path("create_message", MessageCreateView.as_view(), name="create_message"),
]
