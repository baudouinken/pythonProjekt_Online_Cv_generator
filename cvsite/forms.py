from django import forms
from cvsite.models import *
#from django.contrib.auth.models import User


# class UserForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = '__all__'


class DataForm(forms.ModelForm):
    class Meta:
        model = Data
        fields = '__all__'
        exclude = ['user']


class AusbildungForm(forms.ModelForm):
    class Meta:
        model = Ausbildung
        fields = '__all__'
        exclude = ['data']


class BerufForm(forms.ModelForm):
    class Meta:
        model = Beruf
        fields = '__all__'
        exclude = ['data']


class KenntnisseForm(forms.ModelForm):
    class Meta:
        model = Kenntnisse
        fields = '__all__'
        exclude = ['data']


class SprachenForm(forms.ModelForm):
    class Meta:
        model = Sprachen
        fields = '__all__'
        exclude = ['data']


class CVForm(forms.ModelForm):
    class Meta:
        model = Cv
        fields = '__all__'

