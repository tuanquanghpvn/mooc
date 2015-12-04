from django.core.urlresolvers import reverse, reverse_lazy
from django.shortcuts import render
from django.contrib.admin.forms import AdminAuthenticationForm
from django.contrib.admin.forms import PasswordChangeForm
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import (
    FormView, View, CreateView, DetailView,
    UpdateView, DeleteView, TemplateView, ListView,
)
from django.views.generic.detail import SingleObjectMixin
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import permission_required, login_required
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.models import User
from django import forms as djforms
from ars.categories.models import Category
from ars.courses.models import Course, TeacherCourse
from ars.subjects.models import Subject, Session, Task, Enroll
from ars.reviews.models import Review
from ars.blog.models import Blog
from ars.teachers.models import Teacher, ApplyForATeacher
from ars.students.models import Student
from django.core.exceptions import PermissionDenied
from django.db.models import Avg, Count
from . import forms


# Create your views here.
class AdminRequiredMixin(object):
    """docstring for AdminRequiredMixin"""

    @method_decorator(permission_required('is_superuser', login_url='/admin/login/'))
    def dispatch(self, request, *args, **kwargs):
        return super(AdminRequiredMixin, self).dispatch(request, *args, **kwargs)


class TeacherRequiredMixin(object):
    """docstring for TeacherRequiredMixin"""

    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser and not request.user.profile.is_teacher:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


# Function
class LoginRequiredMixin(object):
    """docstring for LoginRequiredMixin"""

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(request, *args, **kwargs)


# Login and dashboard Management

class LoginView(FormView):
    form_class = AdminAuthenticationForm
    template_name = 'admin/login.html'

    def get(self, request, *args, **kwargs):
        user = request.user
        if user.is_active and user.is_staff:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super().get(request, *args, **kwargs)

    def get_success_url(self):
        if self.request.user.profile.is_teacher:
            return reverse_lazy('admin:list_course')
        return reverse_lazy('admin:dashboard')

    def form_valid(self, form):
        admin = form.get_user()
        login(self.request, admin)
        return super().form_valid(form)


class DashboardView(AdminRequiredMixin, TemplateView):
    template_name = 'admin/dashboard_index.html'

    def get_context_data(self, **kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)
        info = {
            'title': 'Dashboard - TMS',
            'sidebar': ['dashboard'],
            'student': Student.objects.count(),
            'course': Course.objects.count(),
            'subject': Subject.objects.count(),
            'teacher': Teacher.objects.count(),

            'top_subject': Enroll.objects.all().annotate(student_count=Count('student'))[0:10],
        }
        context['info'] = info
        return context


class ChangePasswordView(TeacherRequiredMixin, FormView):
    form_class = PasswordChangeForm
    template_name = 'admin/profile.html'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        info = {
            'title': 'Change Password',
        }
        context['info'] = info
        return context

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_success_url(self):
        if self.request.user.profile.is_teacher:
            return reverse_lazy('admin:list_course')
        return reverse_lazy('admin:dashboard')


# Categories Management

class CategoryView(AdminRequiredMixin, ListView):
    """docstring for CategoryView"""
    model = Category
    context_object_name = 'list_category'
    template_name = 'admin/category_index.html'

    def get_context_data(self, **kwargs):
        context = super(CategoryView, self).get_context_data(**kwargs)
        info = {
            'title': 'Category - TMS',
            'sidebar': ['category']
        }
        context['info'] = info
        return context


class CategoryCreateView(AdminRequiredMixin, CreateView):
    """docstring for CategoryCreateView"""
    model = Category
    template_name = 'admin/category_create.html'
    fields = ['name', 'description']

    def get_context_data(self, **kwargs):
        context = super(CategoryCreateView, self).get_context_data(**kwargs)
        info = {
            'title': 'Create Category - TMS',
            'sidebar': ['category']
        }
        context['info'] = info
        return context

    def get_success_url(self):
        return reverse('admin:list_category')


class CategoryUpdateView(AdminRequiredMixin, UpdateView):
    """docstring for CategoryUpdateView"""
    model = Category
    template_name = 'admin/category_update.html'
    fields = ['name', 'description']

    def get_context_data(self, **kwargs):
        context = super(CategoryUpdateView, self).get_context_data(**kwargs)
        info = {
            'title': 'Update Category - TMS',
            'sidebar': ['category']
        }
        context['info'] = info
        return context

    def get_success_url(self):
        return reverse('admin:list_category')


class CategoryDeleteView(AdminRequiredMixin, DeleteView):
    """docstring for CategoryDeleteView"""
    model = Category

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('admin:list_category')


# Courses Management

class CourseView(TeacherRequiredMixin, ListView):
    """docstring for CourseView"""
    model = Course
    context_object_name = 'list_course'
    template_name = 'admin/course_index.html'
    paginate_by = 10

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Course.objects.order_by('-id')
        else:
            return Course.objects.filter(
                teachers=self.request.user.profile.teacher).order_by('-id')

    def get_context_data(self, **kwargs):
        context = super(CourseView, self).get_context_data(**kwargs)
        info = {
            'title': 'Course - TMS',
            'sidebar': ['course']
        }
        context['info'] = info
        return context


class CourseCreateView(TeacherRequiredMixin, CreateView):
    """docstring for CourseCreateView"""
    model = Course
    template_name = 'admin/course_create.html'
    fields = ['name', 'description']

    def get_context_data(self, **kwargs):
        context = super(CourseCreateView, self).get_context_data(**kwargs)
        info = {
            'title': 'Create Course - TMS',
            'sidebar': ['course']
        }
        context['info'] = info
        return context

    def form_valid(self, form):
        course = form.save()
        TeacherCourse.objects.create(
            teacher=self.request.user.profile.teacher,
            course=course, is_creator=True)
        return super(CourseCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse('admin:list_course')


class CourseUpdateView(TeacherRequiredMixin, UpdateView):
    """docstring for CourseUpdateView"""
    model = Course
    template_name = 'admin/course_update.html'
    fields = ['name', 'description']

    def get_context_data(self, **kwargs):
        context = super(CourseUpdateView, self).get_context_data(**kwargs)
        info = {
            'title': 'Update Course - TMS',
            'sidebar': ['course']
        }
        context['info'] = info
        return context

    def get_success_url(self):
        return reverse('admin:list_course')


class CourseDeleteView(TeacherRequiredMixin, DeleteView):
    """docstring for CourseDeleteView"""
    model = Course

    def get(self, request, *args, **kwargs):
        object = self.get_object()
        if request.user.is_superuser or object.creator.profile.user == request.user:
            return self.post(request, *args, **kwargs)
        else:
            raise PermissionDenied

    def get_success_url(self):
        if self.request.user.is_superuser:
            return reverse('admin:list_course')
        else:
            return reverse('admin:list_course_super')


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
        if self.request.user.is_superuser:
            return reverse('admin:list_subject_super')
        else:
            return reverse('admin:list_subject')


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


# Blog Management

class BlogView(TeacherRequiredMixin, ListView):
    """docstring for BlogView"""
    model = Blog
    context_object_name = 'list_blog'
    template_name = 'admin/blog_index.html'
    paginate_by = 10

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Blog.objects.order_by('-id')
        else:
            return Blog.objects.filter(teacher=self.request.user.profile.teacher).order_by('-id')

    def get_context_data(self, **kwargs):
        context = super(BlogView, self).get_context_data(**kwargs)
        info = {
            'title': 'Blog - TMS',
            'sidebar': ['blog']
        }
        context['info'] = info
        return context


class BlogCreateView(TeacherRequiredMixin, CreateView):
    """docstring for BlogCreateView"""
    model = Blog
    template_name = 'admin/blog_create.html'
    fields = ['title', 'description', 'slug', 'content', 'image']

    def get_context_data(self, **kwargs):
        context = super(BlogCreateView, self).get_context_data(**kwargs)
        info = {
            'title': 'Create Blog - TMS',
            'sidebar': ['blog']
        }
        context['info'] = info
        return context

    def form_valid(self, form):
        blog = form.save(commit=False)
        blog.teacher = self.request.user.profile.teacher
        blog.save()
        return super(BlogCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse('admin:list_blog')


class BlogUpdateView(TeacherRequiredMixin, UpdateView):
    """docstring for BlogUpdateView"""
    model = Blog
    template_name = 'admin/blog_update.html'
    fields = ['title', 'description', 'slug', 'content', 'image']

    def get_context_data(self, **kwargs):
        context = super(BlogUpdateView, self).get_context_data(**kwargs)
        info = {
            'title': 'Update Blog - TMS',
            'sidebar': ['blog']
        }
        context['info'] = info
        return context

    def get_success_url(self):
        return reverse('admin:list_blog')


class BlogDeleteView(TeacherRequiredMixin, DeleteView):
    """docstring for BlogDeleteView"""
    model = Blog

    def get(self, request, *args, **kwargs):
        object = self.get_object()
        if request.user.is_superuser or object.teacher.profile.user == request.user:
            return self.post(request, *args, **kwargs)
        else:
            raise PermissionDenied

    def get_success_url(self):
        return reverse('admin:list_blog')


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


# Student Management

class StudentView(AdminRequiredMixin, ListView):
    """docstring for StudentView"""
    context_object_name = 'list_student'
    template_name = 'admin/student_index.html'
    paginate_by = 10

    def get_queryset(self):
        return Student.objects.order_by('-id')

    def get_context_data(self, **kwargs):
        context = super(StudentView, self).get_context_data(**kwargs)
        info = {
            'title': 'Student - TMS',
            'sidebar': ['student']
        }
        context['info'] = info
        return context


class StudentDeleteView(AdminRequiredMixin, DeleteView):
    """docstring for StudentDeleteView"""
    model = User

    def get(self, request, *args, **kwargs):
        # raise Exception
        return self.delete(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('admin:list_student')
