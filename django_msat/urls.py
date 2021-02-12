from django.conf import settings
from django.contrib import admin
from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import include, path
from django.views.generic.base import RedirectView

from assessments import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('mines/', views.MineList.as_view(), name='mines'),
    path('mines/<pk>/', views.MineDetail.as_view(), name='mine-detail'),
    path('questions/', views.AnswerQuestions.as_view(), name='answer-questions'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]