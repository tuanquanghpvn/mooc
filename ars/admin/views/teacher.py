from django.core.urlresolvers import reverse
from django.views.generic import (
    CreateView, UpdateView, DeleteView, ListView,
)
from django.contrib.auth.models import User
from ars.teachers.models import Teacher, ApplyForATeacher
from ars.students.models import Student
from .. import forms
from .dashboard import AdminRequiredMixin


# Teacher Management

class TeacherView(AdminRequiredMixin, ListView):
    """docstring for TeacherView"""
    context_object_name = 'list_teacher'
    template_name = 'admin/teacher_index.html'

    def get_queryset(self):
        return Teacher.objects.all()

    def get_context_data(self, **kwargs):
        context = super(TeacherView, self).get_context_data(**kwargs)
        info = {
            'title': 'Teacher - TMS',
            'sidebar': ['teacher']
        }
        context['info'] = info
        return context


class TeacherCreateView(AdminRequiredMixin, CreateView):
    """docstring for TeacherCreateView"""
    template_name = "admin/teacher_create.html"
    model = User
    form_class = forms.TeacherForm

    def get_context_data(self, **kwargs):
        context = super(TeacherCreateView, self).get_context_data(**kwargs)
        info = {
            'title': 'Create Teacher - TMS',
            'sidebar': ['teacher']
        }
        context['info'] = info
        return context

    def form_valid(self, form):
        password = form.cleaned_data['password']
        description = form.cleaned_data.get('description', None)
        info = form.cleaned_data.get('info', None)
        avatar = form.cleaned_data['avatar']

        user = form.save(commit=False)
        user.is_staff = True
        user.set_password(password)
        user.save()

        user.profile.avatar = avatar
        user.profile.save()

        teacher = Teacher.objects.create(profile=user.profile)
        teacher.info = info
        teacher.description = description
        teacher.save()

        student = Student.objects.get(profile=user.profile)
        student.delete()

        return super(TeacherCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse('admin:list_teacher')


class TeacherUpdateView(AdminRequiredMixin, UpdateView):
    """docstring for TeacherUpdateView"""
    template_name = "admin/teacher_update.html"
    model = User
    form_class = forms.TeacherUpdateForm

    def get_initial(self):
        initial = super().get_initial()
        user_object = self.get_object()
        initial['description'] = user_object.profile.teacher.description
        initial['info'] = user_object.profile.teacher.info
        return initial

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        info = {
            'title': 'Update Teacher - TMS',
            'sidebar': ['teacher']
        }
        context['info'] = info
        return context

    def form_valid(self, form):
        password = form.cleaned_data.get('password', None)
        description = form.cleaned_data.get('description', None)
        info = form.cleaned_data.get('info', None)
        avatar = form.cleaned_data.get('avatar', None)

        user = form.instance

        if password:
            user.set_password(password)

        if avatar:
            user.profile.avatar = avatar
            user.profile.save()

        teacher = Teacher.objects.get(profile=user.profile)
        teacher.info = info
        teacher.description = description
        teacher.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('admin:list_teacher')


class TeacherDeleteView(AdminRequiredMixin, DeleteView):
    """docstring for TeacherDeleteView"""
    model = User

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('admin:list_teacher')


# Apply For A Teacher Management

class ApplyForATeacherView(AdminRequiredMixin, ListView):
    """docstring for ApplyForATeacherView"""
    model = ApplyForATeacher
    context_object_name = 'list_teacher_apply'
    template_name = 'admin/teacher_apply_index.html'
    paginate_by = 10

    def get_queryset(self):
        return ApplyForATeacher.objects.order_by('-id')

    def get_context_data(self, **kwargs):
        context = super(ApplyForATeacherView, self).get_context_data(**kwargs)
        info = {
            'title': 'Apply For A Teacher - TMS',
            'sidebar': ['apply']
        }
        context['info'] = info
        return context


class ApplyForATeacherDeleteView(AdminRequiredMixin, DeleteView):
    """docstring for ApplyForATeacherDeleteView"""
    model = ApplyForATeacher

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('admin:list_teacher_apply')
