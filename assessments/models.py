import uuid as uuid_lib

from django.db import models
from django.contrib.auth.models import User

from django_msat.storage_backends import (PublicMediaStorage, 
    PrivateMediaStorage)

class Company(models.Model):

    name = models.CharField(max_length=255)

    class Meta(object):
        verbose_name_plural = 'Companies'

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

    class Meta(object):
        verbose_name_plural = 'Countries'

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

    def get_absolute_url(self):
        return reverse('mine_detail', kwargs={'pk':self.id})

class QuestionCategory(models.Model):

    order_id = models.IntegerField()
    name = models.CharField(max_length=255)
    about = models.TextField()

    class Meta(object):
        ordering = ('order_id',)
        verbose_name_plural = 'Question categories'

    def __str__(self):
        return self.name

class Question(models.Model):

    order_id = models.IntegerField()
    name = models.CharField(max_length=255)
    category = models.ForeignKey(QuestionCategory, 
        on_delete=models.CASCADE)

    class Meta(object):
        ordering = ('category', 'order_id',)

    def __str__(self):
        return self.name

class Assessment(models.Model):

    uuid = models.UUIDField(db_index=True, 
        default=uuid_lib.uuid4, editable=False)
    date = models.DateTimeField(auto_now_add=True)
    mine = models.ForeignKey(Mine, on_delete=models.CASCADE)
    user = models.ForeignKey(User, 
        on_delete=models.SET_NULL, blank=True, null=True)
    document = models.FileField(storage=PrivateMediaStorage(), 
        upload_to='private/', blank=True, null=True)

    def __str__(self):
        return '{} Assessment'.format(self.mine.name)

class Response(models.Model):

    question = models.ForeignKey(Question, 
        on_delete=models.CASCADE)
    response = models.BooleanField(null=True)
    assessment = models.ForeignKey(Assessment, 
        on_delete=models.CASCADE)

    def __str__(self):
        return self.get_answer()

    def get_answer(self):
        if self.response == True:
            return 'Yes'
        elif self.response == False:
            return 'No'
        return 'N/A'




