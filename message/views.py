from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from message.forms import MessageForm
from message.models import Message


class MessageListView(ListView):
    model = Message
    template_name = "message.html"
    pass

class MessageCreateView(LoginRequiredMixin,CreateView):
    model = Message
    form_class = MessageForm
    template_name = "create_message.html"
    success_url = reverse_lazy("message:message")

    def form_valid(self, form):
        message = form.save(commit=False)
        message.owner = self.request.user
        message.save()
        print(message)
        return super().form_valid(form)
