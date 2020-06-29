from django import forms
from cvsite.models import *


# from django.contrib.auth.models import User


# class UserForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = '__all__'

class DateInput(forms.DateInput):
    input_type = 'date'


class DataForm(forms.ModelForm):
    class Meta:
        model = Data
        fields = '__all__'
        widgets = {'date_of_birth': DateInput()}
        exclude = ['user']


class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = '__all__'
        widgets = {'start': DateInput(), 'end': DateInput()}
        exclude = ['data']


class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = '__all__'
        widgets = {'start': DateInput(), 'end': DateInput()}
        exclude = ['data']


class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = '__all__'
        exclude = ['data']


class LanguageForm(forms.ModelForm):
    class Meta:
        model = Language
        fields = '__all__'
        exclude = ['data']


class CVForm(forms.ModelForm):
    class Meta:
        model = Cv
        fields = '__all__'
        exclude = ['user']
