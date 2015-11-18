"""mooc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

from ars.subjects.views import ListSubjectView


urlpatterns = [
    # url(r'^admin/', include(admin.site.urls)),

    url(r'^$', view=ListSubjectView.as_view(), name='home'),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT, 'show_indexes': settings.DEBUG}),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': settings.DEBUG}),
    
    url(r'^admin/', include('ars.admin.urls', namespace='admin')),
    url(r'^teachers/', include('ars.teachers.urls', namespace='teachers')),
    url(r'^students/', include('ars.students.urls', namespace='students')),
    url(r'^subjects/', include('ars.subjects.urls', namespace='subjects')),
    url(r'^about-us/', include('ars.about.urls', namespace='about')),
    url(r'^contact/', include('ars.contact.urls', namespace='contact')),
    url(r'^blog/', include('ars.blog.urls', namespace='blog')),
    url(r'^category/', include('ars.categories.urls', namespace='category')),
    url(r'^comment/', include('ars.comments.urls', namespace='comment')),
]
