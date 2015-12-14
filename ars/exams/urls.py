from django.conf.urls import include, url

from . import views


urlpatterns = [
    url(r'^$', views.ListExamView.as_view(), name='index'),
    url(r'^take/(?P<pk>[0-9]+)/$', views.TakeExamView.as_view(), name='take'),
]
