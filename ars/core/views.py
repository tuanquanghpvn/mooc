from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.detail import ContextMixin
from django.views.decorators.gzip import gzip_page
from django.http import HttpResponseForbidden
from django.views.decorators.cache import cache_page

from ars.categories.models import Category
from ars.blog.models import Blog
from ars.subjects.models import Subject
from ars.comments.models import Comment

class LoginRequiredMixin(object):
    """docstring for LoginRequiredMixin"""
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class StudentRequiredMixin(object):
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        if not hasattr(request.user.profile, 'student'):
            return HttpResponseForbidden('You must be a student')
        return super().dispatch(request, *args, **kwargs)


class BaseView(ContextMixin):
    """docstring for BaseView"""
    # @method_decorator(cache_page(60 * 15))
    @method_decorator(gzip_page)
    def dispatch(self, request, *args, **kwargs):
        return super(BaseView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(BaseView, self).get_context_data(**kwargs)
        info = {
            'list_lastest_post': Blog.objects.order_by('-id')[:5],
            'list_lastest_subject': Subject.objects.all()[:3],
            'list_popular_subject': Subject.objects.order_by('?')[:3],
            'list_category': Category.objects.all(),
            'list_latest_comment': Comment.objects.order_by('-id')[:3]
        }
        context.update(info)
        return context
