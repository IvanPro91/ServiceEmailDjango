from django.db import models

class Recipient(models.Model):
    email = models.EmailField(verbose_name="Почта")
    full_name = models.CharField(max_length=200, verbose_name="ФИО")
    comments = models.TextField(verbose_name="Комментарий")
