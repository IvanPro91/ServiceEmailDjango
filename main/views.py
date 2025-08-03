from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from mailing.models import Mailing
from message.models import Message
from recipients.models import Recipient


def main_page(request: HttpRequest):
    user = request.user
    context = {
        "count_message": 0,
        "count_mailing": 0,
        "count_recipients": 0,
    }
    if user.is_authenticated:
        if not user.is_superuser:
            context["count_message"] = Message.objects.filter(owner=user.id).count()
            context["count_mailing"] = Mailing.objects.filter(owner=user.id).count()
            context["count_recipients"] = Recipient.objects.filter(
                owner=user.id
            ).count()
        else:
            context["count_message"] = Message.objects.all().count()
            context["count_mailing"] = Mailing.objects.all().count()
            context["count_recipients"] = Recipient.objects.all().count()
    return render(request, template_name="main.html", context=context)
