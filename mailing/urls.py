from django.urls import path

from mailing.apps import MailingConfig
from mailing.views import MailingListView, MailingCreateView

app_name = MailingConfig.name

urlpatterns = [
    path("", MailingListView.as_view(), name="mailing"),
    path("create_mailing", MailingCreateView.as_view(), name="create_mailing"),
]
