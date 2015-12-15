from django.core.urlresolvers import reverse, reverse_lazy
from django.views.generic import ListView, FormView
from django import forms
from django.forms import modelformset_factory
from ars.core.views import BaseView
from ars.exams.models import Exam, Question, Answer
import traceback


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


QuestionFormsetBase = modelformset_factory(Question, fields=('id', 'content',), widgets={'id': forms.HiddenInput,
                                                                                         'content': forms.HiddenInput},
                                           extra=0)
AnswerFormSet = modelformset_factory(Answer, fields=('id', 'content',), widgets={'id': forms.HiddenInput}, extra=0)


class QuestionFormSet(QuestionFormsetBase):
    def add_fields(self, form, index):
        super(QuestionFormSet, self).add_fields(form, index)
        answer = Answer.objects.filter(question__id=form.initial['id'])
        answer = [(x.id, x.content) for x in answer]
        form.fields['answer'] = forms.ChoiceField(choices=answer,
                                                  widget=forms.RadioSelect(attrs={'class': 'field'}))


class TakeExamView(BaseView, FormView):
    template_name = 'exams/take.html'

    def get_form(self, form_class=None):
        category = self.kwargs['pk']
        if self.request.method == 'POST':
            formset = QuestionFormSet(self.request.POST, queryset=Question.objects.filter(category=category))
        else:
            formset = QuestionFormSet(queryset=Question.objects.filter(category=category))
        return formset

    def get_form_kwargs(self):
        category = self.kwargs['pk']
        queryset = Question.objects.filter(category=category)
        kwargs = super().get_form_kwargs()
        kwargs['data'] = self.request.POST
        kwargs['queryset'] = queryset
        return kwargs

    def form_valid(self, form):
        try:
            for frm in form:
                answer = Answer.objects.get(id=frm.cleaned_data['answer'])
                if answer.correct:
                    total_correct = total_correct + 1
        except:
            print(traceback.format_exc())

        return self.render_to_response(self.get_context_data(form=form, total_correct=total_correct))

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

    def get_success_url(self):
        return reverse('exams:index')
