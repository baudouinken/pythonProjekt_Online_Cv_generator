from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.
# home page
def get_home(request):
    return render(request, 'home.html', {'page_title': 'Home CV Generator'})


def get_cv_generator(request):
    ids = ['Photo', 'Name', 'Adress', 'Skills', 'About', 'Experience', 'Education', 'Language']
    templates = {
        "Photo": ['template1/template1_photo.html', 'template2/template2_photo.html', 'template3/template3_photo.html',
                  'template4/template4_photo.html'],
        "Name": ['template1/template1_name.html', 'template2/template2_name.html', 'template3/template3_name.html',
                 'template4/template4_name.html'],
        "Adress": ['template1/template1_adress.html', 'template2/template2_adress.html',
                   'template3/template3_adress.html', 'template4/template4_adress.html'],
        "Skills": ['template1/template1_skills.html', 'template2/template2_skills.html',
                   'template3/template3_skills.html', 'template4/template4_skills.html'],
        "About": ['template1/template1_about.html', 'template2/template2_about.html', 'template3/template3_about.html',
                  'template4/template4_about.html'],
        "Experience": ['template1/template1_experience.html', 'template2/template2_experience.html',
                       'template3/template3_experience.html', 'template4/template4_experience.html'],
        "Education": ['template1/template1_education.html', 'template2/template2_education.html',
                      'template3/template3_education.html', 'template4/template4_education.html'],
        "Language": ['template1/template1_language.html', 'template2/template2_language.html',
                     'template3/template3_language.html', 'template4/template4_language.html']
    }
    return render(request, 'generate_cv.html', {'page_title': 'Generate your CV', 'ids': ids, 'templates': templates})


def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('user_data')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('user_data')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')


@login_required(login_url="/login")
def data_view(request):
    if request.method == 'POST':
        form = DataForm(request.POST, request.FILES)
        if form.is_valid():
            dt = form.save(commit=False)
            dt.user = request.user
            dt.save()
            data_id = dt.id
            return redirect('language', data=data_id)
    else:
        form = DataForm()
    return render(request, 'user_data.html', {'form': form})


def show_data(request):
    data = Data.objects.all()
    return render(request, 'show_data.html', {'page_title': 'User-Data', 'dt': data,
                                              })


def get_user(request):
    user = User.objects.all()
    return render(request, 'user_list.html', {'page_title': 'User', 'usr': user,
                                              })


# Sprachen
def language_view(request, data=None):
    mylanguage = Language.objects.all().filter(data=data)
    if 'next' in request.POST:
        if request.method == 'POST':
            form = LanguageForm(request.POST)
            if form.is_valid():
                lg = form.save(commit=False)
                lg.data_id = data
                lg.save()
                return redirect('skill', data=data)
    elif 'add' in request.POST:
        if request.method == 'POST':
            form = LanguageForm(request.POST)
            if form.is_valid():
                lg = form.save(commit=False)
                lg.data_id = data
                lg.save()
                return redirect('language', data=data)
    else:
        form = LanguageForm()
    return render(request, 'form_language.html', {'form': form, 'mylg': mylanguage, })


# Kenntnisse
def skill_view(request, data=None):
    myskill = Skill.objects.all().filter(data=data)
    if 'next' in request.POST:
        if request.method == 'POST':
            form = SkillForm(request.POST)
            if form.is_valid():
                sk = form.save(commit=False)
                sk.data_id = data
                sk.save()
                return redirect('experience', data=data)
    elif 'add' in request.POST:
        if request.method == 'POST':
            form = SkillForm(request.POST)
            if form.is_valid():
                sk = form.save(commit=False)
                sk.data_id = data
                sk.save()
                return redirect('skill', data=data)
    else:
        form = SkillForm()
    return render(request, 'form_skill.html', {'form': form, 'mysk': myskill, })


# BerufForm
def experience_view(request, data=None):
    myexperience = Experience.objects.all().filter(data=data)
    if 'next' in request.POST:
        if request.method == 'POST':
            form = ExperienceForm(request.POST)
            if form.is_valid():
                exp = form.save(commit=False)
                exp.data_id = data
                exp.save()
                return redirect('education', data=data)
    elif 'add' in request.POST:
        if request.method == 'POST':
            form = ExperienceForm(request.POST)
            if form.is_valid():
                exp = form.save(commit=False)
                exp.data_id = data
                exp.save()
                return redirect('experience', data=data)
    else:
        form = ExperienceForm()
    return render(request, 'form_experience.html', {'form': form, 'myexp': myexperience, })


# Ausbildung
def education_view(request, data=None):
    myeducation = Education.objects.all().filter(data=data)
    if 'next' in request.POST:
        if request.method == 'POST':
            form = EducationForm(request.POST)
            if form.is_valid():
                edu = form.save(commit=False)
                edu.data_id = data
                edu.save()
                return redirect('list_user')
    elif 'add' in request.POST:
        if request.method == 'POST':
            form = EducationForm(request.POST)
            if form.is_valid():
                edu = form.save(commit=False)
                edu.data_id = data
                edu.save()
                return redirect('education', data=data)
    else:
        form = EducationForm()
    return render(request, 'form_education.html', {'form': form, 'myedu': myeducation, })
