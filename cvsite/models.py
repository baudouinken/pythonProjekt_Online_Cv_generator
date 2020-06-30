from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.utils import timezone

from cvsite import fields


class Data(models.Model):
    firstname = models.CharField(max_length=30, blank=False)
    lastname = models.CharField(max_length=30, blank=False)
    date_of_birth = models.DateField(blank=False)  # Wie aendern sie sich?
    place_of_birth = models.CharField(max_length=30, blank=False)
    familystatus = models.CharField(max_length=30, blank=False)
    email = models.EmailField(blank=False)
    tel = models.CharField(blank=False, unique=True, max_length=30)
    adresse = models.CharField(max_length=30, blank=False)
    hobbys = models.CharField(max_length=80, blank=False)  # Wie werden Sie eingegeben # könnte leer sein
    picture = models.ImageField(default='default.png', blank=True)

    user = models.ForeignKey(User, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.firstname} | {self.lastname} | {self.date_of_birth} | {self.place_of_birth} | {self.familystatus} | ' \
               f'{self.email} | {self.tel} | {self.adresse} | {self.hobbys}'  # | {self.user}'


class Language(models.Model):
    language = models.CharField(max_length=20, blank=False)
    level = fields.IntegerRangeField("Level - from 0 - 10", min_value=0, max_value=10, default=0)
    data = models.ForeignKey(Data, on_delete=models.CASCADE)


class Education(models.Model):
    certificate = models.CharField(max_length=100)
    start = models.DateField()
    end = models.DateField()
    institution = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    data = models.ForeignKey(Data, on_delete=models.CASCADE)


class Experience(models.Model):
    start = models.DateField()
    end = models.DateField()
    institution = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    data = models.ForeignKey(Data, on_delete=models.CASCADE)


class Skill(models.Model):
    skill = models.CharField(max_length=100)
    level = fields.IntegerRangeField("Level - from 0 - 10", min_value=0, max_value=10, default=0)
    data = models.ForeignKey(Data, on_delete=models.CASCADE)


class Cv(models.Model):
    name = models.CharField(max_length=30, default='unnamed')
    description = models.CharField(max_length=100, default='', blank=True)
    template_adresse = models.CharField(max_length=100)
    template_education = models.CharField(max_length=100)
    template_experience = models.CharField(max_length=100)
    template_language = models.CharField(max_length=100)
    template_name = models.CharField(max_length=100)
    template_photo = models.CharField(max_length=100)
    template_skills = models.CharField(max_length=100)
    user = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    datetime = models.DateTimeField(default=timezone.now)
