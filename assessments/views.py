from django.shortcuts import redirect, render
from django.views.generic import DetailView, ListView, View

from assessments.models import (Mine, Company,
    QuestionCategory, Question, Assessment, Response)

def home(request):
    return render(request, 'home.html')

class MineList(ListView):
    model = Mine

class MineDetail(DetailView):
    model = Mine

class AssessmentDetail(DetailView):
    model = Assessment

class AnswerQuestions(ListView):
    model = Question

    def post(self, request):
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
        for key, value in request.POST.items():
            print(value)
            try:
                pk, resp = key.split('_')
                print(key, pk, resp)
                question = Question.objects.get(id=int(pk))
                response = Response.objects.create(
                       question=question,
                       response=self.get_response(resp),
                       assessment=assessment
                    )
            except Exception as error:
                print(error)
        return redirect('/')

    def get_response(self, response):
        if response == 'true':
            return True
        else:
            return False

