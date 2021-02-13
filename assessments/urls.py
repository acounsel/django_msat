from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('mines/', views.MineList.as_view(), name='mine_list'),
    path('mines/<pk>/', views.MineDetail.as_view(), name='mine_detail'),
    path('questions/', views.AnswerQuestions.as_view(), name='answer_questions'),
    path('assessment/<pk>/', views.AssessmentDetail.as_view(), name='assessment_detail')
]