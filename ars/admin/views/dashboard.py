from django.core.urlresolvers import reverse_lazy
from django.contrib.admin.forms import AdminAuthenticationForm
from django.contrib.admin.forms import PasswordChangeForm
from django.http import HttpResponseRedirect
from django.views.generic import (
    FormView, TemplateView
)
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import permission_required, login_required
from django.utils.decorators import method_decorator
from django.contrib.auth import login
from ars.courses.models import Course
from ars.subjects.models import Subject, Session, Enroll
from ars.teachers.models import Teacher
from ars.students.models import Student
from django.core.exceptions import PermissionDenied
from django.db.models import Count


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
        top_subject = Enroll.objects.values('session').annotate(student_count=Count('student')).order_by(
            'student_count')
        list_top = []
        for item in top_subject:
            obj = {
                'session': Session.objects.get(id=item['session']),
                'student_count': item['student_count'],
            }
            list_top.append(obj)

        info = {
            'title': 'Dashboard - TMS',
            'sidebar': ['dashboard'],
            'student': Student.objects.count(),
            'course': Course.objects.count(),
            'subject': Subject.objects.count(),
            'teacher': Teacher.objects.count(),

            'top_subject': list_top,
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
