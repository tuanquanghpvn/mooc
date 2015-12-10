from django.core.urlresolvers import reverse
from django.views.generic import (
    CreateView, UpdateView, DeleteView, ListView,
)
from ars.courses.models import Course, TeacherCourse
from django.core.exceptions import PermissionDenied
from .dashboard import TeacherRequiredMixin


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
        return reverse('admin:list_course')
