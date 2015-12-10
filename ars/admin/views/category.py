from django.core.urlresolvers import reverse
from django.views.generic import (
    CreateView, UpdateView, DeleteView, ListView,
)
from ars.categories.models import Category
from .dashboard import AdminRequiredMixin


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
