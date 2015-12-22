from django.db import models
from django.conf import settings
from ars.core.models import Timestampable, Describable
from ars.subjects.models import Subject
from ars.categories.models import Category
from ars.teachers.models import Teacher


class Group(Describable, Timestampable):
    class Meta:
        db_table = 'group'

    def __str__(self):
        return self.name


# Create your models here.
class Question(Timestampable):
    CHOICE_QUESTION = (
        (1, 'One choice'),
        (2, 'Multiple choice')
    )

    CHOICE_LEVEL = (
        (1, 'Level 1'),
        (2, 'Level 2'),
        (3, 'Level 3')
    )

    teacher = models.ForeignKey(Teacher)
    group = models.ForeignKey(Group)
    content = models.CharField(max_length=500)
    code = models.TextField(blank=True, default='')
    level = models.IntegerField(choices=CHOICE_LEVEL, default=1)
    type = models.IntegerField(choices=CHOICE_QUESTION, default=1)

    class Meta:
        db_table = 'question'


class Answer(models.Model):
    question = models.ForeignKey(Question, related_name='answers')
    content = models.CharField(max_length=255)
    correct = models.BooleanField()

    class Meta:
        db_table = 'answer'


class Exam(Describable, Timestampable):
    CHOICE_LEVEL = (
        (1, 'Level 1'),
        (2, 'Level 2'),
        (3, 'Level 3')
    )

    teacher = models.ForeignKey(Teacher)
    group = models.ForeignKey(Group)
    num_question = models.IntegerField()
    minute = models.IntegerField()
    level = models.IntegerField(choices=CHOICE_LEVEL, default=1)
    fill = models.BooleanField(blank=False, default=False)
    image = models.ImageField(upload_to=settings.EXAM_DIR, max_length=255, default='', blank=False)

    def get_image_url(self):
        if self.image:
            return self.image.url
        return settings.DEFAULT_EXAMPLE

    class Meta:
        db_table = 'exam'
