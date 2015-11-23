from django.conf.urls import include, url

from . import views


urlpatterns = [
    url(r'^$', views.ListTeacherView.as_view(), name='index'),
    url(r'^create/$', views.CreateTeacherApplyView.as_view(), name='create'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailTeacherView.as_view(), name='detail'),
]
