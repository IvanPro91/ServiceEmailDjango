from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic import ListView, DetailView, DeleteView, UpdateView

from mailing.forms import MessageForm
from mailing.models import Mailing, Message


class MailingListView(ListView):
    model = Mailing
    template_name = "mailing.html"
    pass

class MessageListView(ListView):
    model = Message
    template_name = "message.html"
    pass

class MailingCreateView(CreateView):
    model = Mailing
    template_name = "create_mailing.html"
    fields = "__all__"


class MessageCreateView(LoginRequiredMixin,CreateView):
    model = Message
    form_class = MessageForm
    template_name = "create_message.html"
    success_url = reverse_lazy("mailing:message")

    def form_valid(self, form):
        message = form.save(commit=False)
        message.owner = self.request.user
        message.save()
        print(message)
        return super().form_valid(form)

class MailingDetailView(DetailView):
    pass


class MailingDeleteView(DeleteView):
    pass


class MailingUpdateView(UpdateView):
    pass

