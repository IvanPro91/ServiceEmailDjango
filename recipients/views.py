from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView

from recipients.models import Recipient


class RecipientsListView(ListView):
    model = Recipient
    template_name = "recipients.html"
    pass


class RecipientsDetailView(DetailView):
    pass


class RecipientsDeleteView(DeleteView):
    pass


class RecipientsUpdateView(UpdateView):
    pass


class RecipientsCreateView(CreateView):
    pass
