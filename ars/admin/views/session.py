from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic import (
    CreateView
)
from django.contrib import messages
from ars.subjects.models import Session
from .dashboard import TeacherRequiredMixin


# Sessions Management

class SessionCreateView(TeacherRequiredMixin, CreateView):
    """docstring for SessionCreateView"""
    model = Session
    fields = ['subject', 'start_date', 'end_date']

    def form_valid(self, form):
        self.subject = form.cleaned_data['subject']
        start_date = form.cleaned_data['start_date']
        end_date = form.cleaned_data['end_date']
        if end_date < start_date:
            messages.add_message(self.request, messages.INFO, {'id': 'session', 'msg': 'End date need > start date'})
            return HttpResponseRedirect(self.get_success_url())
        self.object = form.save()
        return super(SessionCreateView, self).form_valid(form)

    def form_invalid(self, form):
        self.subject = form.cleaned_data['subject']
        messages.add_message(self.request, messages.INFO, {'id': 'session', 'msg': 'All fields is required'})
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse_lazy('admin:detail_subject', kwargs={'pk': self.subject.pk})
