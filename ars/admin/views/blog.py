from django.core.urlresolvers import reverse
from django.views.generic import (
    CreateView, UpdateView, DeleteView, ListView
)
from ars.blog.models import Blog
from django.core.exceptions import PermissionDenied
from .dashboard import TeacherRequiredMixin


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
