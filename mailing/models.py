from django.db import models

from message.models import Message
from recipients.models import Recipient
from user.models import User


class Mailing(models.Model):
    message = models.ForeignKey(Message, verbose_name="Сообщение", on_delete=models.CASCADE)
    recipients = models.ManyToManyField(Recipient, verbose_name="Получатели сообщения")
    status_ending = models.BooleanField(default=False, verbose_name="Общий статус")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")
    owner = models.ForeignKey(User, verbose_name="Владелец рассылки", on_delete=models.CASCADE)


