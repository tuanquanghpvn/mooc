from django.db import models
from ars.core.models import Timestampable, Describable
from ars.subjects.models import Subject
from ars.categories.models import Category
from ars.teachers.models import Teacher


# Create your models here.
class Question(Timestampable):
    teacher = models.ForeignKey(Teacher)
    category = models.ForeignKey(Category)
    content = models.CharField(max_length=255)

    class Meta:
        db_table = 'question'


class Answer(models.Model):
    question = models.ForeignKey(Question, related_name='answers')
    content = models.CharField(max_length=255)
    correct = models.BooleanField()

    class Meta:
        db_table = 'answer'


class Exam(Describable, Timestampable):
    teacher = models.ForeignKey(Teacher)
    subject = models.ForeignKey(Subject)
    category = models.ForeignKey(Category)
    num_question = models.IntegerField()

    class Meta:
        db_table = 'exam'