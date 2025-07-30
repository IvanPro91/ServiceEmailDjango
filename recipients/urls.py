from django.urls import path

from recipients.apps import RecipientsConfig
from recipients.views import RecipientsListView

app_name = RecipientsConfig.name

urlpatterns = [
    path("", RecipientsListView.as_view(), name="recipients"),
]
