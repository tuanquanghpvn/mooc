from django.core.urlresolvers import reverse
from django.views.generic import (
    DeleteView, ListView
)
from django.contrib.auth.models import User
from ars.students.models import Student
from .dashboard import AdminRequiredMixin


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
