from django.contrib import admin

from assessments import models

admin.site.register(models.Mine)
admin.site.register(models.QuestionCategory)
admin.site.register(models.Question)
admin.site.register(models.Assessment)
admin.site.register(models.Response)