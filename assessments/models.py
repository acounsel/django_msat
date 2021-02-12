from django.db import models
from django.contrib.auth.models import User

from django_msat.storage_backends import (PublicMediaStorage, 
    PrivateMediaStorage)

class Mine(models.Model):

    site_name = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.site_name

class QuestionCategory(models.Model):

    order_id = models.IntegerField()
    name = models.CharField(max_length=255)
    about = models.TextField()

    def __str__(self):
        return self.name

class Question(models.Model):

    order_id = models.IntegerField()
    name = models.CharField(max_length=255)
    category = models.ForeignKey(QuestionCategory, 
        on_delete=models.CASCADE)

    def __str__(self):
        return self.category.name + ": " + self.name

class Assessment(models.Model):

    date = models.DateTimeField(auto_now_add=True)
    mine = models.ForeignKey(Mine, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    document = models.FileField(storage=PrivateMediaStorage(), 
        upload_to='private/', blank=True, null=True)

    def __str__(self):
        return self.mine.site_name + ' Assessment: ' + self.user.first_name

class Response(models.Model):

    question = models.ForeignKey(Question, 
        on_delete=models.CASCADE)
    response = models.BooleanField()
    assessment = models.ForeignKey(Assessment, 
        on_delete=models.CASCADE)

    def __str__(self):
        question = self.question.name
        return question + ' ' + self.get_answer()

    def get_answer(self):
        if self.response == True:
            return 'Yes'
        else:
            return 'No'




