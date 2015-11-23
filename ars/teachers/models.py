from django.db import models
from django.conf import settings

from ars.core.models import UserProfile, Timestampable


class Teacher(models.Model):
    profile = models.OneToOneField(UserProfile,
                                default=None, related_name='teacher')
    description = models.TextField(blank=True, default='')
    info = models.TextField(blank=True, default='')

    class Meta:
        db_table = 'teacher'

    def __str__(self):
        return 'Teacher {}'.format(self.name)

    @property
    def username(self):
        try:
            return self.profile.user.username
        except:
            return ''

    @property
    def full_name(self):
        try:
            if self.profile.user.get_full_name():
                return self.profile.user.get_full_name()
            else:
                return self.profile.user.username
        except:
            return self.profile.user.username

    @property
    def avatar(self):
        if self.profile.avatar:
            return self.profile.avatar.url
        return settings.DEFAULT_IMAGE 

class ApplyForATeacher(Timestampable):
    full_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.full_name

    class Meta:
        db_table = 'apply_for_a_teacher'
