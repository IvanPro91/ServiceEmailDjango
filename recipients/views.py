from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView

from recipients.forms import RecipientForm
from recipients.models import Recipient


class RecipientsListView(ListView):
    model = Recipient
    template_name = "recipients.html"
    pass

class RecipientsCreateView(CreateView):
    model = Recipient
    form_class = RecipientForm
    template_name = "create_recipient.html"
    success_url = reverse_lazy("recipients:recipients")


class RecipientsDetailView(DetailView):
    pass


class RecipientsDeleteView(DeleteView):
    model = Recipient
    template_name = "delete_recipient.html"
    success_url = reverse_lazy("recipients:recipients")

class RecipientsUpdateView(UpdateView):
    pass


