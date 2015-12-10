from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic import (
    CreateView, UpdateView, DeleteView
)
from django.contrib import messages
from ars.subjects.models import Session, Task
from django.core.exceptions import PermissionDenied
from .dashboard import TeacherRequiredMixin


# Task Management

class TaskCreateView(TeacherRequiredMixin, CreateView):
    """docstring for TaskCreateView"""
    model = Task
    fields = ['session', 'name', 'slug', 'content', 'start_date',
              'end_date', 'link_youtube']

    def get_context_data(self, **kwargs):
        context = super(TaskCreateView, self).get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        self.session = form.cleaned_data['session']
        start_date = form.cleaned_data['start_date']
        end_date = form.cleaned_data['end_date']
        if end_date < start_date:
            messages.add_message(self.request, messages.INFO, "End date need > start date")
            return HttpResponseRedirect(self.get_success_url())
        self.object = form.save()
        return super(TaskCreateView, self).form_valid(form)

    def form_invalid(self, form):
        self.session = form.cleaned_data['session']
        messages.add_message(self.request, messages.INFO, "All fields is required")
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse_lazy('admin:detail_subject', kwargs={'pk': self.session.subject.pk})


class TaskUpdateView(TeacherRequiredMixin, UpdateView):
    model = Task
    fields = ['session', 'name', 'slug', 'content', 'start_date',
              'end_date', 'link_youtube']
    template_name = 'admin/task_update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        info = {
            'title': 'Update Task - TMS',
            'sidebar': ['subject']
        }
        context['info'] = info
        context['sessions'] = Session.objects.filter(subject=self.object.session.subject)
        return context

    def get_success_url(self):
        return reverse_lazy('admin:detail_subject', kwargs={'pk': self.object.session.subject.id})


class TaskDeleteView(TeacherRequiredMixin, DeleteView):
    """docstring for TaskDeleteView"""
    model = Task

    def get(self, request, *args, **kwargs):
        object = self.get_object()
        if request.user.is_superuser or object.session.subject.course.creator.profile.user == request.user:
            return self.post(request, *args, **kwargs)
        else:
            raise PermissionDenied

    def get_success_url(self):
        return reverse_lazy('admin:detail_subject', kwargs={'pk': self.object.session.subject.pk})
