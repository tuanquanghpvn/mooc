from django.db import models
from ars.core.models import Timestampable, Describable
from ars.subjects.models import Subject
from ars.categories.models import Category


# Create your models here.
class Question(Timestampable):
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
    subject = models.ForeignKey(Subject)
    questions = models.ManyToManyField(Question, related_name='exams', db_table='exam_question')

    class Meta:
        db_table = 'exam'
