from django.core.urlresolvers import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic import (
    FormView, CreateView, DetailView,
    UpdateView, DeleteView, ListView,
)
from django.views.generic.detail import SingleObjectMixin
from django import forms as djforms
from ars.courses.models import Course
from ars.subjects.models import Subject, Session, Task, Enroll
from ars.reviews.models import Review
from django.core.exceptions import PermissionDenied
from .. import forms
from .dashboard import TeacherRequiredMixin


# Subjects Management

class SubjectView(TeacherRequiredMixin, ListView):
    """docstring for SubjectView"""
    model = Subject
    context_object_name = 'list_subject'
    template_name = 'admin/subject_index.html'
    paginate_by = 10

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Subject.objects.order_by('-id')
        else:
            return Subject.objects.filter(
                course__teachers=self.request.user.profile.teacher).order_by('-id')

    def get_context_data(self, **kwargs):
        context = super(SubjectView, self).get_context_data(**kwargs)
        info = {
            'title': 'Subject - TMS',
            'sidebar': ['subject']
        }
        context['info'] = info
        return context


class SubjectCreateView(TeacherRequiredMixin, CreateView):
    """docstring for SubjectCreateView"""
    model = Subject
    template_name = 'admin/subject_create.html'
    form_class = forms.SubjectForm

    def get(self, request, *args, **kwargs):
        self.object = None
        form = self.get_form()
        form.fields['course'] = djforms.ModelChoiceField(
            queryset=Course.objects.filter(teachers__profile__user=self.request.user), widget=djforms.widgets.Select(
                attrs={'class': 'form-control select2',
                       'style': 'width: 100%;'}))
        return self.render_to_response(self.get_context_data(form=form))

    def get_context_data(self, **kwargs):
        context = super(SubjectCreateView, self).get_context_data(**kwargs)
        info = {
            'title': 'Create Subject - TMS',
            'sidebar': ['subject']
        }
        context['info'] = info
        return context

    def form_invalid(self, form):
        form.fields['course'] = djforms.ModelChoiceField(
            queryset=Course.objects.filter(teachers__profile__user=self.request.user), widget=djforms.widgets.Select(
                attrs={'class': 'form-control select2',
                       'style': 'width: 100%;'}))
        return super().form_invalid(form)

    def get_success_url(self):
        return reverse('admin:list_subject')


class SubjectUpdateView(TeacherRequiredMixin, UpdateView):
    """docstring for SubjectUpdateView"""
    model = Subject
    template_name = 'admin/subject_update.html'
    form_class = forms.SubjectForm

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if self.request.user.is_superuser:
            form.fields['course'] = djforms.ModelChoiceField(
                queryset=Course.objects.filter(teachers=self.object.course.creator),
                widget=djforms.widgets.Select(
                    attrs={'class': 'form-control select2',
                           'style': 'width: 100%;'}))
        else:
            form.fields['course'] = djforms.ModelChoiceField(
                queryset=Course.objects.filter(teachers__profile__user=self.request.user),
                widget=djforms.widgets.Select(
                    attrs={'class': 'form-control select2',
                           'style': 'width: 100%;'}))
        return self.render_to_response(self.get_context_data(form=form))

    def get_context_data(self, **kwargs):
        context = super(SubjectUpdateView, self).get_context_data(**kwargs)
        info = {
            'title': 'Update Subject - TMS',
            'sidebar': ['subject']
        }
        context['info'] = info
        return context

    def form_invalid(self, form):
        form.fields['course'] = djforms.ModelChoiceField(
            queryset=Course.objects.filter(teachers__profile__user=self.request.user), widget=djforms.widgets.Select(
                attrs={'class': 'form-control select2',
                       'style': 'width: 100%;'}))
        return super().form_invalid(form)

    def get_success_url(self):
        return reverse('admin:list_subject')


class CommonContextSubject(object):
    model = Subject
    template_name = 'admin/subject_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        info = {
            'title': 'Detail Subject - TMS',
            'sidebar': ['subject']
        }
        context['info'] = info

        context['reviews'] = Review.objects.filter(subject=self.object).order_by('-id')
        context['sessions'] = Session.objects.filter(subject=self.object).order_by('-id')
        context['tasks'] = Task.objects.filter(session__subject=self.object).order_by('-id')
        context['endrolls'] = Enroll.objects.filter(session__subject=self.object).order_by('-id')
        return context


class CreateTaskSubmit(TeacherRequiredMixin, CommonContextSubject,
                       SingleObjectMixin, FormView):
    form_class = forms.TaskForm

    def get_success_url(self):
        return reverse_lazy('admin:detail_subject',
                            kwargs={'pk': self.object.pk})

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        self.task = form.save()
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form):
        return self.render_to_response(
            self.get_context_data(task_form=form, cur_form=True))


class CreateSessionSubmit(TeacherRequiredMixin, CommonContextSubject,
                          SingleObjectMixin, FormView):
    form_class = forms.SessionForm

    def get_success_url(self):
        return reverse_lazy('admin:detail_subject', kwargs={'pk': self.object.pk})

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        self.session = form.save()
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form):
        return self.render_to_response(
            self.get_context_data(session_form=form, cur_form=False))


class SubjectDetailView(TeacherRequiredMixin, CommonContextSubject, DetailView):
    task_form = forms.TaskForm
    session_form = forms.SessionForm
    cur_form = True

    def post(self, request, *args, **kwargs):
        if 'submit_task' in request.POST:
            view = CreateTaskSubmit.as_view()
        elif 'submit_session' in request.POST:
            view = CreateSessionSubmit.as_view()

        try:
            return view(request, *args, **kwargs)
        except NameError as err:
            return super().post(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task_form'] = self.task_form
        context['session_form'] = self.session_form
        context['cur_form'] = self.cur_form
        return context


class SubjectDeleteView(TeacherRequiredMixin, DeleteView):
    """docstring for SubjectDeleteView"""
    model = Subject

    def get(self, request, *args, **kwargs):
        object = self.get_object()
        if request.user.is_superuser or object.course.creator.profile.user == request.user:
            return self.post(request, *args, **kwargs)
        else:
            raise PermissionDenied

    def get_success_url(self):
        return reverse('admin:list_subject')
