from django.db import models
from ars.students.models import Student
from ars.subjects.models import Subject
from ars.core.models import Timestampable


# Create your models here.
class Review(Timestampable):
    MAX_STARS = 5
    RATING_STARS = (
        (1, 'One star'),
        (2, 'Two stars'),
        (3, 'Three stars'),
        (4, 'Four stars'),
        (5, 'Five stars'),
    )

    student = models.ForeignKey(Student, related_name='reviews')
    subject = models.ForeignKey(Subject, related_name='reviews')
    rating = models.IntegerField(choices=RATING_STARS, default=4)
    content = models.TextField()

    class Meta:
        verbose_name = "Review"
        verbose_name_plural = "Reviews"
        db_table = "review"

    def __str__(self):
        pass
