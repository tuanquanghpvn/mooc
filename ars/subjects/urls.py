from django.conf.urls import include, url

from . import views


urlpatterns = [
    url(r'^$', view=views.ListSubjectView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', view=views.DetailSubjectView.as_view(), name='detail'),
    url(r'^task/(?P<pk>[0-9]+)/$', view=views.DetailTaskView.as_view(), name='task'),
    url(r'^enroll/$', view=views.EnrollSubjectView.as_view(), name='enroll'),
]
