import traceback

from django.core.urlresolvers import reverse
from django.views.generic import (
    CreateView, UpdateView, DeleteView, ListView
)
from django.core.exceptions import PermissionDenied

from ars.courses.models import Course
from .dashboard import TeacherRequiredMixin
from django import forms
from django.forms import modelformset_factory, formset_factory, BaseFormSet, BaseModelFormSet
from django.db import transaction
from ars.exams.models import Answer, Exam, Question
from ars.subjects.models import Subject
from ars.categories.models import Category


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('content', 'category')

        widgets = {
            'category': forms.widgets.Select(
                attrs={'class': 'form-control custom-select2',
                       'style': 'width: 100%;'}),
        }


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ('content', 'correct')

        widgets = {
            'content': forms.widgets.TextInput(
                attrs={'class': 'form-control custom-select2',
                       'style': 'width: 100%;', 'placeholder': 'Enter answer'}),
        }


class RequiredFormSet(BaseFormSet):
    def __init__(self, *args, **kwargs):
        super(RequiredFormSet, self).__init__(*args, **kwargs)
        for form in self.forms:
            form.empty_permitted = False


class RequiredModelFormSet(BaseModelFormSet):
    def __init__(self, *args, **kwargs):
        super(RequiredModelFormSet, self).__init__(*args, **kwargs)
        for form in self.forms:
            form.empty_permitted = False


AnswerFormSet = formset_factory(AnswerForm, extra=4, formset=RequiredFormSet)

AnswerUpdateFormSet = modelformset_factory(Answer, formset=RequiredModelFormSet, fields=('content', 'correct'),
                                           widgets={
                                               'content': forms.widgets.TextInput(
                                                   attrs={'class': 'form-control custom-select2',
                                                          'style': 'width: 100%;',
                                                          'placeholder': 'Enter answer'}),
                                           }, max_num=4)


# Question Management

class QuestionView(TeacherRequiredMixin, ListView):
    """docstring for QuestionView"""
    model = Question
    context_object_name = 'list_question'
    template_name = 'admin/question_index.html'
    paginate_by = 10

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Question.objects.order_by('-id')
        else:
            return Question.objects.filter(teacher=self.request.user.profile.teacher).order_by('-id')

    def get_context_data(self, **kwargs):
        context = super(QuestionView, self).get_context_data(**kwargs)
        info = {
            'title': 'Question - TMS',
            'sidebar': ['question']
        }
        context['info'] = info
        return context


class QuestionCreateView(TeacherRequiredMixin, CreateView):
    """docstring for QuestionCreateView"""
    model = Question
    template_name = 'admin/question_create.html'
    form_class = QuestionForm

    def get_context_data(self, **kwargs):
        context = super(QuestionCreateView, self).get_context_data(**kwargs)
        info = {
            'title': 'Create Question - TMS',
            'sidebar': ['question']
        }
        context.setdefault('formset', AnswerFormSet)
        context['info'] = info
        return context

    def form_valid(self, form):
        with transaction.atomic():
            question = form.save(commit=False)
            question.teacher = self.request.user.profile.teacher
            question.save()

            formset = AnswerFormSet(self.request.POST)
            if formset.is_valid():
                for form in formset:
                    aws = form.save(commit=False)
                    aws.question = question
                    aws.save()

        return super(QuestionCreateView, self).form_valid(form)

    def form_invalid(self, form):
        formset = AnswerFormSet(self.request.POST)
        return self.render_to_response(
            self.get_context_data(form=form,
                                  formset=formset))

    def get_success_url(self):
        return reverse('admin:list_question')


class QuestionUpdateView(TeacherRequiredMixin, UpdateView):
    """docstring for QuestionUpdateView"""
    model = Question
    template_name = 'admin/question_update.html'
    form_class = QuestionForm

    def get_context_data(self, **kwargs):
        context = super(QuestionUpdateView, self).get_context_data(**kwargs)
        info = {
            'title': 'Update Question - TMS',
            'sidebar': ['question']
        }
        context.setdefault('formset', AnswerUpdateFormSet(queryset=Answer.objects.filter(question=self.object)))
        context['info'] = info
        return context

    def form_valid(self, form):
        try:
            with transaction.atomic():
                form.save()
                formset = AnswerUpdateFormSet(self.request.POST, queryset=Answer.objects.filter(question=self.object))
                if formset.is_valid():
                    formset.save()
        except:
            print(traceback.format_exc())
        return super(QuestionUpdateView, self).form_valid(form)

    def form_invalid(self, form):
        formset = AnswerUpdateFormSet(self.request.POST, queryset=Answer.objects.filter(question=self.object))
        return self.render_to_response(
            self.get_context_data(form=form,
                                  formset=formset))

    def get_success_url(self):
        return reverse('admin:list_question')


class QuestionDeleteView(TeacherRequiredMixin, DeleteView):
    """docstring for QuestionDeleteView"""
    model = Question

    def get(self, request, *args, **kwargs):
        object = self.get_object()
        if request.user.is_superuser or object.teacher.profile.user == request.user:
            return self.post(request, *args, **kwargs)
        else:
            raise PermissionDenied

    def get_success_url(self):
        return reverse('admin:list_question')


# Exam Management

class ExamForm(forms.ModelForm):
    class Meta:
        model = Exam
        fields = ('subject', 'name', 'category', 'description', 'num_question', 'minute')

        widgets = {
            'category': forms.widgets.Select(
                attrs={'class': 'form-control select2',
                       'style': 'width: 100%;', 'placeholder': 'Enter category'}),
            'subject': forms.widgets.Select(
                attrs={'class': 'form-control select2',
                       'style': 'width: 100%;', 'placeholder': 'Enter subject'}),
        }

    def clean(self):
        cleaned_data = super(ExamForm, self).clean()
        category = cleaned_data.get('category', None)
        count = Question.objects.filter(category=category).count()
        if count == 0 and category:
            self.add_error('category', "You don't have question in category selected!")
        # elif count < 10:
        #     self.add_error('category', "You need more 10 question in category!")


class ExamView(TeacherRequiredMixin, ListView):
    """docstring for ExamView"""
    model = Question
    context_object_name = 'list_exam'
    template_name = 'admin/exam_index.html'
    paginate_by = 10

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Exam.objects.order_by('-id')
        else:
            return Exam.objects.filter(teacher=self.request.user.profile.teacher).order_by('-id')

    def get_context_data(self, **kwargs):
        context = super(ExamView, self).get_context_data(**kwargs)
        info = {
            'title': 'Exam - TMS',
            'sidebar': ['exam']
        }
        context['info'] = info
        return context


class ExamCreateView(TeacherRequiredMixin, CreateView):
    """docstring for ExamCreateView"""
    model = Exam
    template_name = 'admin/exam_create.html'
    form_class = ExamForm

    def get(self, request, *args, **kwargs):
        self.object = None
        course_list = Course.objects.filter(teachers__profile__user=self.request.user)
        djform = self.get_form()
        djform.fields['subject'] = forms.ModelChoiceField(
            queryset=Subject.objects.filter(course__in=course_list),
            widget=forms.widgets.Select(
                attrs={'class': 'form-control select2',
                       'style': 'width: 100%;'}))
        return self.render_to_response(self.get_context_data(form=djform))

    def get_context_data(self, **kwargs):
        context = super(ExamCreateView, self).get_context_data(**kwargs)
        info = {
            'title': 'Create Exam - TMS',
            'sidebar': ['exam']
        }
        context['info'] = info
        return context

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.teacher = self.request.user.profile.teacher
        instance.save()
        return super(ExamCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse('admin:list_exam')


class ExamUpdateView(TeacherRequiredMixin, UpdateView):
    """docstring for ExamUpdateView"""
    model = Exam
    template_name = 'admin/exam_update.html'
    form_class = ExamForm

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        course_list = Course.objects.filter(teachers=self.object.teacher)
        djform = self.get_form()
        djform.fields['subject'] = forms.ModelChoiceField(
            queryset=Subject.objects.filter(course__in=course_list),
            widget=forms.widgets.Select(
                attrs={'class': 'form-control select2',
                       'style': 'width: 100%;'}))
        return self.render_to_response(self.get_context_data(form=djform))

    def get_context_data(self, **kwargs):
        context = super(ExamUpdateView, self).get_context_data(**kwargs)
        info = {
            'title': 'Update Exam - TMS',
            'sidebar': ['exam']
        }
        context['info'] = info
        return context

    def get_success_url(self):
        return reverse('admin:list_exam')


class ExamDeleteView(TeacherRequiredMixin, DeleteView):
    """docstring for ExamDeleteView"""
    model = Exam

    def get(self, request, *args, **kwargs):
        object = self.get_object()
        if request.user.is_superuser or object.creator.profile.user == request.user:
            return self.post(request, *args, **kwargs)
        else:
            raise PermissionDenied

    def get_success_url(self):
        return reverse('admin:list_exam')
