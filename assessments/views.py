from django.shortcuts import redirect, render
from django.views.generic import DetailView, ListView, View

from assessments.models import (Mine, 
    QuestionCategory, Question, Assessment, Response)

def home(request):
    return render(request, 'home.html')

class MineList(ListView):
    model = Mine

class MineDetail(DetailView):
    model = Mine

class AnswerQuestions(ListView):
    model = Question

    def post(self, request):
        print(request.POST)
        for key, value in request.POST.items():
            try:
                question = Question.objects.get(id=int(key))
                response = Response.objects.create(
                       question=question,
                       response=True,
                       assessment=Assessment.objects.first()
                    )
            except:
                pass
        return redirect('/')