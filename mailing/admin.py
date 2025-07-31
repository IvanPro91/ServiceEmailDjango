from django.contrib import admin

from mailing.models import RecipientMailing, Message, Mailing

@admin.register(RecipientMailing)
class RecipientMailingAdmin(admin.ModelAdmin):
    list_display = tuple(n_meta.name for n_meta in RecipientMailing._meta.fields)

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = tuple(n_meta.name for n_meta in Message._meta.fields)

@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = tuple(n_meta.name for n_meta in Mailing._meta.fields)