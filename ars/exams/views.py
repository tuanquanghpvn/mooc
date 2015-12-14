from django.core.urlresolvers import reverse, reverse_lazy
from django.views.generic import ListView, FormView
from django import forms
from django.forms import formset_factory, modelformset_factory
from ars.core.views import BaseView
from ars.exams.models import Exam, Question, Answer


class ListExamView(BaseView, ListView):
    model = Exam
    template_name = 'exams/list.html'
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        info = {
            'info': {
                'title': 'Example',
            },
            'page_title': 'Example',
        }
        context.update(info)
        return context


QuestionFormsetBase = modelformset_factory(Question, fields=('id', 'content',), widgets={'id': forms.HiddenInput}, extra=0, can_order=True)
AnswerFormSet = modelformset_factory(Answer, fields=('id', 'content',), widgets={'id': forms.HiddenInput}, extra=0)


class QuestionFormSet(QuestionFormsetBase):
    def add_fields(self, form, index):
        super(QuestionFormSet, self).add_fields(form, index)
        answer = Answer.objects.filter(question__id=form.initial['id'])
        answer = [(x.id, x.content) for x in answer]
        form.fields['answer'] = forms.ChoiceField(choices=answer)


class TakeExamView(BaseView, FormView):
    template_name = 'exams/take.html'

    def get_form(self, form_class=None):
        category = self.kwargs['pk']
        formset = QuestionFormSet(queryset=Question.objects.filter(category=category))
        return formset

    def form_valid(self, form):
        pass

    def form_invalid(self, form):
        pass

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        info = {
            'info': {
                'title': 'Take Example',
            },
            'page_title': 'Take Example',
        }
        context.update(info)
        return context
