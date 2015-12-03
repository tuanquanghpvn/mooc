from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.DashboardView.as_view(), name='dashboard'),
    url(r'^profile/$', views.ChangePasswordView.as_view(),
        name='profile'),
    url(r'^login/$', views.LoginView.as_view(), name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout',
        {'next_page': '/admin/login/'}, name='logout'),

    #############################################################
    #############################################################
    #############################################################
    # Url category
    url(r'^category/$', views.CategoryView.as_view(), name='list_category'),
    url(r'^category/create/$', views.CategoryCreateView.as_view(),
        name='create_category'),
    url(r'^category/update/(?P<pk>[0-9]+)/$',
        views.CategoryUpdateView.as_view(), name='update_category'),
    url(r'^category/delete/(?P<pk>[0-9]+)/$',
        views.CategoryDeleteView.as_view(), name='delete_category'),

    #############################################################
    #############################################################
    #############################################################
    # Url course
    url(r'^course/$', views.CourseView.as_view(), name='list_course'),
    url(r'^course-super/$', views.CourseSuperView.as_view(), name='list_course_super'),
    url(r'^course/create/$', views.CourseCreateView.as_view(),
        name='create_course'),
    url(r'^course/update/(?P<pk>[0-9]+)/$', views.CourseUpdateView.as_view(),
        name='update_course'),
    url(r'^course/delete/(?P<pk>[0-9]+)/$', views.CourseDeleteView.as_view(),
        name='delete_course'),

    #############################################################
    #############################################################
    #############################################################
    # Url subject
    url(r'^subject/$', views.SubjectView.as_view(), name='list_subject'),
    url(r'^subject-super/$', views.SubjectSuperView.as_view(), name='list_subject_super'),
    url(r'^subject/create/$', views.SubjectCreateView.as_view(),
        name='create_subject'),
    url(r'^subject/update/(?P<pk>[0-9]+)/$', views.SubjectUpdateView.as_view(),
        name='update_subject'),
    url(r'^subject/detail/(?P<pk>[0-9]+)/$', views.SubjectDetailView.as_view(),
        name='detail_subject'),
    url(r'^subject/detail-super/(?P<pk>[0-9]+)/$', views.SubjectSuperDetailView.as_view(),
        name='detail_subject_super'),
    url(r'^subject/delete/(?P<pk>[0-9]+)/$', views.SubjectDeleteView.as_view(),
        name='delete_subject'),

    url(r'^session/create/$', views.SessionCreateView.as_view(),
        name='create_session'),
    url(r'^task/create/$', views.TaskCreateView.as_view(),
        name='create_task'),
    url(r'^task/update/(?P<pk>[0-9]+)/$', views.TaskUpdateView.as_view(),
        name='update_task'),
    url(r'^task/delete/(?P<pk>[0-9]+)/$', views.TaskDeleteView.as_view(),
        name='delete_task'),

    #############################################################
    #############################################################
    #############################################################
    # Url blog
    url(r'^blog/$', views.BlogView.as_view(), name='list_blog'),
    url(r'^blog-super/$', views.BlogSuperView.as_view(), name='list_blog_super'),
    url(r'^blog/create/$', views.BlogCreateView.as_view(), name='create_blog'),
    url(r'^blog/update/(?P<pk>[0-9]+)/$', views.BlogUpdateView.as_view(),
        name='update_blog'),
    url(r'^blog/delete/(?P<pk>[0-9]+)/$', views.BlogDeleteView.as_view(),
        name='delete_blog'),

    #############################################################
    #############################################################
    #############################################################
    # Url teacher
    url(r'^teacher/$', views.TeacherView.as_view(), name='list_teacher'),
    url(r'^teacher/create/$', views.TeacherCreateView.as_view(),
        name='create_teacher'),
    url(r'^teacher/update/(?P<pk>[0-9]+)/$', views.TeacherUpdateView.as_view(),
        name='update_teacher'),
    # url(r'^blog/update/(?P<pk>[0-9]+)/$', views.BlogUpdateView.as_view(), 
    #                                                     name='update_blog'),
    url(r'^teacher/delete/(?P<pk>[0-9]+)/$', views.TeacherDeleteView.as_view(),
        name='delete_teacher'),

    url(r'^teacher-apply/$', views.ApplyForATeacherView.as_view(), name='list_teacher_apply'),
    url(r'^teacher-apply/delete/(?P<pk>[0-9]+)/$', views.ApplyForATeacherDeleteView.as_view(),
        name='delete_teacher_apply'),

    #############################################################
    #############################################################
    #############################################################
    # Url student
    url(r'^student/$', views.StudentView.as_view(), name='list_student'),
    url(r'^student/delete/(?P<pk>[0-9]+)/$', views.StudentDeleteView.as_view(),
        name='delete_student'),
]
