from django.db import models
from django.contrib.auth.models import User

from django_msat.storage_backends import (PublicMediaStorage, 
    PrivateMediaStorage)

class Company(models.Model):

    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Country(models.Model):
    AMERICA = 'america'
    EUROPE = 'europe'
    AFRICA = 'africa'
    ASIA = 'asia'
    OCEANIA = 'oceania'
    REGION_CHOICES = (
        (AMERICA, 'Americas'),
        (EUROPE, 'Europe'),
        (AFRICA, 'Africa'),
        (ASIA, 'Asia'),
        (OCEANIA, 'Oceania')
    )

    name = models.CharField(max_length=255)
    region = models.CharField(max_length=100,
        choices=REGION_CHOICES, blank=True, null=True)

    def __str__(self):
        return self.name

class Mine(models.Model):

    name = models.CharField(max_length=255)
    company = models.ForeignKey(Company, 
        on_delete=models.SET_NULL, blank=True, null=True)
    country = models.ForeignKey(Country,
        on_delete=models.SET_NULL, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name

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
    response = models.BooleanField(null=True)
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




