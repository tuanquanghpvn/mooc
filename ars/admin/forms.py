from django import forms
from django.conf import settings
from django.contrib.auth.models import User

from ars.subjects.models import Subject
from ars.core.models import UserProfile
from ars.subjects.models import Task, Session

import re

class SubjectForm(forms.ModelForm):
    """docstring for SubjectForm"""
    class Meta:
        model = Subject
        fields = ('categories', 'course', 'name', 'slug',
                    'description', 'image')

        widgets = {
            'categories': forms.widgets.SelectMultiple(
                attrs={'class': 'form-control select2',
                        'style': 'width: 100%;',
                        'multiple': "multiple"}),

            'course': forms.widgets.Select(
                attrs={'class': 'form-control select2',
                        'style': 'width: 100%;'}),            
        }


class TeacherForm(forms.ModelForm):
    re_password = forms.CharField(max_length=500)
    description = forms.CharField(required=False)
    info = forms.CharField(required=False)
    avatar = forms.ImageField(required=False, max_length=255)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password', 'email')

    def clean(self):
        cleaned_data = super(TeacherForm, self).clean()
        password = cleaned_data.get("password")
        re_password = cleaned_data.get("re_password")

        if password != re_password:
            msg = "Password not contrain."
            self.add_error('re_password', msg)

class TeacherUpdateForm(forms.ModelForm):
    password = forms.CharField(max_length=500, required=False)
    re_password = forms.CharField(max_length=500, required=False)
    description = forms.CharField(required=False)
    info = forms.CharField(required=False)
    avatar = forms.ImageField(required=False, max_length=255)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        re_password = cleaned_data.get("re_password")

        if password != re_password:
            msg = "Password not contrain."
            self.add_error('re_password', msg)

class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ('session', 'name', 'slug',
                    'content', 'start_date', 'end_date',
                    'link_youtube')

    def youtube_url_validation(self, url):
        youtube_regex = (
            r'(https?://)?(www\.)?'
            '(youtube|youtu|youtube-nocookie)\.(com|be)/'
            '(watch\?v=|embed/|v/|.+\?v=)?([^&=%\?]{11})'
        )

        youtube_regex_match = re.match(youtube_regex, url)
        if youtube_regex_match:
            return youtube_regex_match.group(6)

        return False

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get('start_date', False)
        end_date = cleaned_data.get('end_date', False)
        link_youtube = cleaned_data.get('link_youtube', False)

        if start_date and end_date and start_date > end_date:
            msg = "'End date' must be later than 'Start date'"
            self.add_error('start_date', msg)
            self.add_error('end_date', msg)

        if link_youtube and not self.youtube_url_validation(link_youtube):
            msg = "Youtube link not validate"
            self.add_error('link_youtube', msg)

        return cleaned_data    

class SessionForm(forms.ModelForm):

    class Meta:
        model = Session
        fields = ('subject', 'start_date', 'end_date')

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get('start_date', False)
        end_date = cleaned_data.get('end_date', False)

        if start_date and end_date and start_date > end_date:
            msg = "'End date' must be later than 'Start date'"
            self.add_error('start_date', msg)
            self.add_error('end_date', msg)

        return cleaned_data
