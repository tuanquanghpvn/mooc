from django.db import models
from django.conf import settings

from ars.categories.models import Category
from ars.courses.models import Course
from ars.students.models import Student
from ars.core.models import Describable, Timestampable


class Subject(Describable, Timestampable):
    course = models.ForeignKey(Course)
    categories = models.ManyToManyField(Category, db_table="category_subject", related_name='subjects')
    slug = models.SlugField(max_length=255)
    image = models.ImageField(upload_to=settings.SUBJECT_DIR, max_length=255, default='', blank=False)

    class Meta:
        verbose_name = "Subject"
        verbose_name_plural = "Subjects"
        db_table = 'subject'

    def get_image_url(self):
        if self.image:
            return self.image.url
        return settings.DEFAULT_IMAGE

    def __str__(self):
        return self.name

    @property
    def latest_session(self):
        try:
            session = self.sessions.order_by('-id')[0]
        except:
            session = None
        return session

class Session(models.Model):
    subject = models.ForeignKey(Subject, related_name='sessions')
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    class Meta:
        verbose_name = "Session"
        verbose_name_plural = "Sessions"
        db_table = 'session'

    def __str__(self):
        return '{} - {}'.format(self.start_date, self.end_date)
    
class Task(Describable):
    session = models.ForeignKey(Session, related_name='tasks')
    slug = models.SlugField(max_length=255)
    content = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    link_youtube = models.URLField(max_length=255, default='', blank=False)

    class Meta:
        verbose_name = "Task"
        verbose_name_plural = "Tasks"
        db_table = 'task'

    def __str__(self):
        return 'Task {}'.format(self.name)

    def get_image_url(self):
        if self.image:
            return self.image.url
        return settings.DEFAULT_IMAGE
    
    @property
    def is_published(self):
        return True

class Enroll(Timestampable):
    session = models.ForeignKey(Session, related_name='enrolls')
    student = models.ForeignKey(Student)

    class Meta:
        verbose_name = "Enroll"
        verbose_name_plural = "Enrolls"
        db_table = 'enroll'

    def __str__(self):
        return 'Student {} enrolled subject {}, start on {}'.format(
                                self.profile.user.username,
                                self.session.subject.name,
                                self.session.start_date)
