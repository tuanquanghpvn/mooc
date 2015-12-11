from django.conf.urls import url
from .views import (
    blog, category, course, dashboard, session, subject,
    task, teacher, student, exam
)

urlpatterns = [
    url(r'^$', dashboard.DashboardView.as_view(), name='dashboard'),
    url(r'^profile/$', dashboard.ChangePasswordView.as_view(),
        name='profile'),
    url(r'^login/$', dashboard.LoginView.as_view(), name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout',
        {'next_page': '/admin/login/'}, name='logout'),

    #############################################################
    #############################################################
    #############################################################
    # Url category
    url(r'^category/$', category.CategoryView.as_view(), name='list_category'),
    url(r'^category/create/$', category.CategoryCreateView.as_view(),
        name='create_category'),
    url(r'^category/update/(?P<pk>[0-9]+)/$',
        category.CategoryUpdateView.as_view(), name='update_category'),
    url(r'^category/delete/(?P<pk>[0-9]+)/$',
        category.CategoryDeleteView.as_view(), name='delete_category'),

    #############################################################
    #############################################################
    #############################################################
    # Url course
    url(r'^course/$', course.CourseView.as_view(), name='list_course'),
    url(r'^course/create/$', course.CourseCreateView.as_view(),
        name='create_course'),
    url(r'^course/update/(?P<pk>[0-9]+)/$', course.CourseUpdateView.as_view(),
        name='update_course'),
    url(r'^course/delete/(?P<pk>[0-9]+)/$', course.CourseDeleteView.as_view(),
        name='delete_course'),

    #############################################################
    #############################################################
    #############################################################
    # Url subject
    url(r'^subject/$', subject.SubjectView.as_view(), name='list_subject'),
    url(r'^subject/create/$', subject.SubjectCreateView.as_view(),
        name='create_subject'),
    url(r'^subject/update/(?P<pk>[0-9]+)/$', subject.SubjectUpdateView.as_view(),
        name='update_subject'),
    url(r'^subject/detail/(?P<pk>[0-9]+)/$', subject.SubjectDetailView.as_view(),
        name='detail_subject'),
    url(r'^subject/delete/(?P<pk>[0-9]+)/$', subject.SubjectDeleteView.as_view(),
        name='delete_subject'),

    url(r'^session/create/$', session.SessionCreateView.as_view(),
        name='create_session'),

    url(r'^task/create/$', task.TaskCreateView.as_view(),
        name='create_task'),
    url(r'^task/update/(?P<pk>[0-9]+)/$', task.TaskUpdateView.as_view(),
        name='update_task'),
    url(r'^task/delete/(?P<pk>[0-9]+)/$', task.TaskDeleteView.as_view(),
        name='delete_task'),

    #############################################################
    #############################################################
    #############################################################
    # Url blog
    url(r'^blog/$', blog.BlogView.as_view(), name='list_blog'),
    url(r'^blog/create/$', blog.BlogCreateView.as_view(), name='create_blog'),
    url(r'^blog/update/(?P<pk>[0-9]+)/$', blog.BlogUpdateView.as_view(),
        name='update_blog'),
    url(r'^blog/delete/(?P<pk>[0-9]+)/$', blog.BlogDeleteView.as_view(),
        name='delete_blog'),

    #############################################################
    #############################################################
    #############################################################
    # Url teacher
    url(r'^teacher/$', teacher.TeacherView.as_view(), name='list_teacher'),
    url(r'^teacher/create/$', teacher.TeacherCreateView.as_view(),
        name='create_teacher'),
    url(r'^teacher/update/(?P<pk>[0-9]+)/$', teacher.TeacherUpdateView.as_view(),
        name='update_teacher'),
    # url(r'^blog/update/(?P<pk>[0-9]+)/$', views.BlogUpdateView.as_view(), 
    #                                                     name='update_blog'),
    url(r'^teacher/delete/(?P<pk>[0-9]+)/$', teacher.TeacherDeleteView.as_view(),
        name='delete_teacher'),

    url(r'^teacher-apply/$', teacher.ApplyForATeacherView.as_view(), name='list_teacher_apply'),
    url(r'^teacher-apply/delete/(?P<pk>[0-9]+)/$', teacher.ApplyForATeacherDeleteView.as_view(),
        name='delete_teacher_apply'),

    #############################################################
    #############################################################
    #############################################################
    # Url student
    url(r'^student/$', student.StudentView.as_view(), name='list_student'),
    url(r'^student/delete/(?P<pk>[0-9]+)/$', student.StudentDeleteView.as_view(),
        name='delete_student'),

    #############################################################
    #############################################################
    #############################################################
    # Url question
    url(r'^question/$', exam.QuestionView.as_view(), name='list_question'),
    url(r'^question/create/$', exam.QuestionCreateView.as_view(),
        name='create_question'),
    url(r'^question/update/(?P<pk>[0-9]+)/$', exam.QuestionUpdateView.as_view(),
        name='update_question'),
    url(r'^question/delete/(?P<pk>[0-9]+)/$', exam.QuestionDeleteView.as_view(),
        name='delete_question'),

    #############################################################
    #############################################################
    #############################################################
    # Url exam
    url(r'^exam/$', exam.ExamView.as_view(), name='list_exam'),
    url(r'^exam/create/$', exam.ExamCreateView.as_view(),
        name='create_exam'),
    url(r'^exam/update/(?P<pk>[0-9]+)/$', exam.ExamUpdateView.as_view(),
        name='update_exam'),
    url(r'^exam/delete/(?P<pk>[0-9]+)/$', exam.ExamDeleteView.as_view(),
        name='delete_exam'),
]
