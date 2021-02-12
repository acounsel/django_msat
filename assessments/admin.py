from django.contrib import admin

from assessments import models

admin.site.register(models.Company)
admin.site.register(models.QuestionCategory)

@admin.register(models.Country)
class CountryAdmin(admin.ModelAdmin):
    list_items = (
        'name',
        'region',
    )
    list_display = list_items
    list_display_links = list_items
    list_filter = ('region',)

@admin.register(models.Mine)
class MineAdmin(admin.ModelAdmin):
    list_items = (
        'name',
        'company',
        'country',
        'location',
    )
    list_display = list_items
    list_display_links = list_items
    list_filter = ('company','country')

@admin.register(models.Question)
class QuestionAdmin(admin.ModelAdmin):
    list_items = (
        'order_id',
        'name',
        'category'
    )
    list_display = list_items
    list_display_links = list_items
    list_filter = ('category',)

@admin.register(models.Assessment)
class AssessmentAdmin(admin.ModelAdmin):
    list_items = (
        'date',
        'mine',
        'user'
    )
    list_display = list_items
    list_display_links = list_items
    list_filter = ('mine','user')

@admin.register(models.Response)
class ResponseAdmin(admin.ModelAdmin):
    list_items = (
        'assessment',
        'question',
        'response',
    )
    list_display = list_items
    list_display_links = list_items
    list_filter = ('question', 'question__category', 
        'assessment__mine')

