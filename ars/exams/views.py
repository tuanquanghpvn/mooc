from django.core.urlresolvers import reverse, reverse_lazy
from django.views.generic import ListView, FormView
from django import forms
from django.forms import modelformset_factory
from ars.core.views import BaseView
from ars.exams.models import Exam, Question, Answer
from datetime import datetime
from ars.core import utils
from datetime import timedelta
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


QuestionFormsetBase = modelformset_factory(Question, fields=('id', 'content', 'type', 'level'),
                                           widgets={'id': forms.HiddenInput,
                                                    'content': forms.HiddenInput,
                                                    'type': forms.HiddenInput,
                                                    'level': forms.HiddenInput},
                                           extra=0)
AnswerFormSet = modelformset_factory(Answer, fields=('id', 'content',), widgets={'id': forms.HiddenInput}, extra=0)


class QuestionFormSet(QuestionFormsetBase):
    def add_fields(self, form, index):
        super(QuestionFormSet, self).add_fields(form, index)
        answer = Answer.objects.filter(question__id=form.initial['id'], question__level__lte=form.initial['level'])
        answer = [(x.id, x) for x in answer]

        # One choice
        if form.initial['type'] == 1:
            form.fields['answer'] = forms.ChoiceField(choices=answer,
                                                      widget=forms.RadioSelect(attrs={'class': 'field'}))
        # Multiple choice
        elif form.initial['type'] == 2:
            form.fields['answer'] = forms.MultipleChoiceField(choices=answer,
                                                              widget=forms.CheckboxSelectMultiple(
                                                                  attrs={'class': 'field'}))


class TakeExamView(BaseView, FormView):
    template_name = 'exams/take.html'

    def get_form(self, form_class=None):
        exam = Exam.objects.get(id=self.kwargs['pk'])
        group = exam.group
        if self.request.method == 'POST':
            formset = QuestionFormSet(self.request.POST)
        else:
            # queryset = Question.objects.filter(group=group)
            queryset = Question.objects.filter(group=group, teacher=exam.teacher).order_by('?')[
                       :exam.num_question]
            formset = QuestionFormSet(queryset=queryset)
        return formset

    def get_form_kwargs(self):
        exam = Exam.objects.get(id=self.kwargs['pk'])
        group = exam.group
        queryset = Question.objects.filter(group=group, teacher=exam.teacher)[:exam.num_question]
        kwargs = super().get_form_kwargs()
        kwargs['data'] = self.request.POST
        kwargs['queryset'] = queryset
        return kwargs

    def form_valid(self, form):
        total_correct = 0
        try:
            exam = Exam.objects.get(id=self.kwargs['pk'])
            message = self.request.POST.get('time_make_exam')
            if exam.minute != 0 and not self.check_valid_time(message, exam.minute):
                return self.render_to_response(
                    self.get_context_data(form=form, message="Time make exam is expired!"))

            for frm in form:
                if frm.cleaned_data['type'] == 1:
                    answer = Answer.objects.get(id=frm.cleaned_data['answer'])
                    if answer.correct:
                        total_correct = total_correct + 1
                elif frm.cleaned_data['type'] == 2:
                    list_answer = frm.cleaned_data['answer']
                    question = frm.cleaned_data['id']
                    count_question_correct = Answer.objects.filter(question__id=question).filter(correct=True).count()
                    if len(list_answer) == count_question_correct:
                        success = True
                        for answer_check in list_answer:
                            answer_data = Answer.objects.get(id=answer_check)
                            if not answer_data.correct:
                                success = False
                        if success:
                            total_correct = total_correct + 1
        except:
            print(traceback.format_exc())

        return self.render_to_response(self.get_context_data(form=form, total_correct=total_correct))

    def form_invalid(self, form):
        total_correct = 0
        try:
            exam = Exam.objects.get(id=self.kwargs['pk'])
            message = self.request.POST.get('time_make_exam')
            if exam.minute != 0 and not self.check_valid_time(message, exam.minute):
                return self.render_to_response(
                    self.get_context_data(form=form, message="Time make exam is expired!"))

            for frm in form:
                if 'answer' in frm.cleaned_data:
                    answer = Answer.objects.get(id=frm.cleaned_data['answer'])
                    if answer.correct:
                        total_correct = total_correct + 1
        except:
            print(traceback.format_exc())

        return self.render_to_response(self.get_context_data(form=form, total_correct=str(total_correct)))

    def check_valid_time(self, data, minute):
        try:
            parse_date = utils.decryption(data)
            time_make_exam = datetime.strptime(parse_date, "%Y-%m-%d %H:%M:%S.%f")
            cal_time = datetime.now() - timedelta(minutes=minute)
            if cal_time <= time_make_exam:
                return True
            return False
        except:
            print(traceback.format_exc())
            return False

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        info = {
            'info': {
                'title': 'Take Example',
            },
            'page_title': 'Take Example',
        }
        if self.request.method == 'GET':
            context['time_make_exam'] = utils.encryption(str(datetime.now()))
        else:
            context['time_make_exam'] = self.request.POST.get('time_make_exam')
        context.update(info)
        context['exam'] = Exam.objects.get(id=self.kwargs['pk'])
        return context

    def get_success_url(self):
        return reverse('exams:index')
