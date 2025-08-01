from django.forms.boundfield import BoundWidget
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic import ListView, DetailView, DeleteView, UpdateView

from mailing.forms import MailingForm
from mailing.models import Mailing
from recipients.models import Recipient


class MailingListView(ListView):
    model = Mailing
    template_name = "mailing.html"


class MailingCreateView(CreateView):
    model = Mailing
    form_class = MailingForm
    template_name = "create_mailing.html"
    success_url = reverse_lazy("mailing:mailing")

    def form_valid(self, form):
        mailing: Mailing = form.save(commit=False)
        mailing.owner = self.request.user
        mailing.save()
        form.save_m2m()
        return super().form_valid(form)

class MailingDetailView(DetailView):
    pass


class MailingDeleteView(DeleteView):
    pass


class MailingUpdateView(UpdateView):
    pass

