from django.contrib import messages
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import DetailView, ListView, View

from assessments.models import (Mine, Company,
    QuestionCategory, Question, Assessment, Response)

class Home(ListView):
    model = Mine

class MineDetail(DetailView):
    model = Mine

class AssessmentList(ListView):
    model = Assessment

class AssessmentDetail(DetailView):
    model = Assessment

class AnswerQuestions(ListView):
    model = Question

    def post(self, request):
        company, mine, assessment = self.get_assessment(request)
        for key, value in request.POST.items():
            self.create_response(key, value, assessment)
        self.add_null_responses(assessment)
        messages.success(request, 
            'Assessment Received; Thank You!')
        return redirect(reverse('home'))

    def get_assessment(self, request):
        company, created = Company.objects.get_or_create(
            name=request.POST.get('company')
        )
        mine, created = Mine.objects.get_or_create(
            name=request.POST.get('mine'),
            company=company,
            location=request.POST.get('location')
        )
        assessment = Assessment.objects.create(
            mine=mine,
            user=request.user
        )
        return company, mine, assessment

    def create_response(self, key, value, assessment):
        try:
            pk, resp = key.split('_')
            question = Question.objects.get(id=int(pk))
            response = Response.objects.create(
                   question=question,
                   response=self.get_response(resp),
                   assessment=assessment
                )
        except Exception as error:
            print(error)

    def get_response(self, response):
        if response == 'true':
            return True
        else:
            return False

    def add_null_responses(self, assessment):
        remaining_questions = Question.objects.exclude(
            response__assessment=assessment).distinct()
        for question in remaining_questions:
            Response.objects.create(
                assessment=assessment,
                question=question,
            )


