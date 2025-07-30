from django.db import models

from recipients.models import Recipient
from user.models import User


class RecipientMailing(models.Model):
    recipient = models.ForeignKey(Recipient, verbose_name="Получатели", null=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

class Message(models.Model):
    theme = models.CharField(max_length=150, verbose_name="Тема письма")
    body = models.TextField(verbose_name="Тело письма")
    owner = models.ForeignKey(User, verbose_name="Владелец письма", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

class Mailing(models.Model):
    message = models.ForeignKey(Message, verbose_name="Сообщение", on_delete=models.CASCADE)
    recipients = models.ForeignKey(RecipientMailing, verbose_name="Получатели сообщения", on_delete=models.CASCADE)
    status_ending = models.BooleanField(default=False, verbose_name="Общий статус")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")
    owner = models.ForeignKey(User, verbose_name="Владелец рассылки", on_delete=models.CASCADE)


