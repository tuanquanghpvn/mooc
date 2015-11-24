from django.core.urlresolvers import reverse, reverse_lazy
from django.views.generic import DetailView, ListView, CreateView
from django.http import HttpResponseRedirect, HttpResponsePermanentRedirect
from django.contrib import messages
from django import forms
from captcha.fields import ReCaptchaField

from ars.core.views import BaseView
from ars.teachers.models import Teacher, ApplyForATeacher

class TeacherApplyForm(forms.ModelForm):
    """docstring for TeacherApplyForm"""
    # captcha = ReCaptchaField()

    class Meta:
        model = ApplyForATeacher
        fields = ('full_name', 'email', 'phone')

class CreateTeacherApplyView(BaseView, CreateView):
    model = ApplyForATeacher
    form_class = TeacherApplyForm

    def form_valid(self, form):
        form.save()
        messages.add_message(self.request, messages.INFO, "Apply Teacher Success ! Thanks for support !")
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, "Apply Teacher Error !")
        return HttpResponseRedirect(self.get_success_url())        

    def get_success_url(self):
        return reverse_lazy('teachers:index')

class DetailTeacherView(BaseView, DetailView):
    model = Teacher
    template_name = 'teachers/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        info = {
            'info': {
                'title': self.object.username,
            },
            'page_title': self.object.username,
        }
        context.update(info)
        return context


class ListTeacherView(BaseView, ListView):
    model = Teacher
    template_name = 'teachers/list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        info = {
            'info': {
                'title': 'Teachers',
            },
            'page_title': 'Teachers',
        }
        context.update(info)
        return context
