from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView

from mailing.models import Mailing


class MailingListView(ListView):
    model = Mailing
    template_name = "mailing.html"
    pass


class MailingDetailView(DetailView):
    pass


class MailingDeleteView(DeleteView):
    pass


class MailingUpdateView(UpdateView):
    pass


class MailingCreateView(CreateView):
    pass
