from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from .forms import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.
# home page
def get_home(request):
    return render(request, 'home.html', {'page_title': 'Home CV Generator'})


def about_us(request):
    return render(request, 'Aboutus.html', {'page_title': 'About Us'})


@login_required(login_url="/login")
def mycvs(request):
    try:
        cvs = Cv.objects.filter(user=request.user)
        data = Data.objects.get(user=request.user)
        return render(request, 'mycvs.html', {'page_title': 'My CVs', 'cvs': cvs, 'data': data})
    except Data.DoesNotExist:
        messages.error(request, 'Please insert your data first.')
        return redirect('user_data')


@login_required(login_url="/login")
def get_cv_generator(request, pk=None):
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
    try:
        data = Data.objects.get(user=request.user)
    except Data.DoesNotExist:
        messages.error(request, 'Please insert your data first.')
        return redirect('user_data')

    try:
        cv = Cv.objects.get(pk=pk)  # old cv from mycvs
        form = CVForm(instance=cv)
    except Cv.DoesNotExist:
        cv = False
        form = CVForm()  # standard

    if request.method == 'POST':
        if 'save' in request.POST:  # save
            form = CVForm(request.POST)
            if form.is_valid():
                cv_new = form.save(commit=False)
                cv_new.user = request.user
                cv_new.save()
                return redirect('mycvs')
            else:  # error
                return redirect('generatecv')
    return render(request, 'generate_cv.html',
                  {'page_title': 'Generate your CV', 'ids': ids, 'templates': templates,
                   'data': data,
                   'skills': Skill.objects.filter(data=data),
                   'languages': Language.objects.filter(data=data),
                   'experience': Experience.objects.filter(data=data),
                   'education': Education.objects.filter(data=data),
                   'form': form,
                   'cv': cv})


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
            try:
                dt = Data.objects.get(user=user)
                dt_id = dt.id
                return render(request, 'home.html', {'page_title': 'Home CV Generator', })
            except Data.DoesNotExist:
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
    user1 = request.user
    if request.method == 'POST':
        form = DataForm(request.POST, request.FILES)
        if form.is_valid():
            dt = form.save(commit=False)
            dt.user = request.user
            dt.save()
            messages.success(request, 'Data saved')
            data_id = dt.id
            return redirect('language', data=data_id)
    else:
        try:
            du = Data.objects.get(user=user1)
            form = DataForm(instance=du)
        except Data.DoesNotExist:
            form = DataForm()
    return render(request, 'user_data.html', {'form': form})


def next_data(request):
    try:
        usr = request.user
        dt = Data.objects.get(user=usr)
        dt_id = dt.id
        return redirect('language', data=dt_id)
    except Data.DoesNotExist:
        messages.error(request, 'Please insert your data first.')
        return redirect('user_data')


# Sprachen
def language_view(request, data=None):
    mylanguage = Language.objects.all().filter(data=data)
    if 'add' in request.POST:
        if request.method == 'POST':
            form = LanguageForm(request.POST)
            if form.is_valid():
                lg = form.save(commit=False)
                lg.data_id = data
                lg.save()
                messages.success(request, 'Language saved')
                return redirect('language', data=data)
    else:
        form = LanguageForm()
    return render(request, 'form_language.html', {'form': form, 'mylg': mylanguage, })


def next_lang(request):
    try:
        usr = request.user
        dt = Data.objects.get(user=usr)
        dt_id = dt.id
        return redirect('skill', data=dt_id)
    except Data.DoesNotExist:
        messages.error(request, 'Please insert your data first.')
        return redirect('user_data')


def check_lang(request):
    try:
        usr = request.user
        dt = Data.objects.get(user=usr)
        dt_id = dt.id
        return redirect('language', data=dt_id)
    except Data.DoesNotExist:
        messages.error(request, 'Please insert your data first.')
        return redirect('user_data')


def language_edit(request, data=None, pk=None):
    mylanguage = Language.objects.all().filter(data=data)
    if pk:
        lg = Language.objects.get(pk=pk)
    else:
        lg = Language()

    if 'save' in request.POST:
        if request.method == 'POST':
            form = LanguageForm(request.POST, instance=lg)
            if form.is_valid():
                lg = form.save(commit=False)
                lg.data_id = data
                lg.save()
                messages.success(request, 'Language edited')
                return redirect('language', data=data)
    else:
        form = LanguageForm(instance=lg)
    return render(request, 'language_edit.html', {'form': form, 'mylg': mylanguage, })


def language_delete(request, data=None, pk=None):
    if pk:
        lg = Language.objects.get(pk=pk)
    else:
        lg = Language()

    if lg:
        lg.delete()
        messages.warning(request, 'Language deleted')
        return redirect('language', data=data)
    else:
        form = LanguageForm()
    return render(request, 'form_language.html', {'form': form, })


# Kenntnisse
def skill_view(request, data=None):
    myskill = Skill.objects.all().filter(data=data)
    if 'add' in request.POST:
        if request.method == 'POST':
            form = SkillForm(request.POST)
            if form.is_valid():
                sk = form.save(commit=False)
                sk.data_id = data
                sk.save()
                messages.success(request, 'Skill saved')
                return redirect('skill', data=data)
    else:
        form = SkillForm()
    return render(request, 'form_skill.html', {'form': form, 'mysk': myskill, })


def next_skill(request):
    try:
        usr = request.user
        dt = Data.objects.get(user=usr)
        dt_id = dt.id
        return redirect('experience', data=dt_id)
    except Data.DoesNotExist:
        messages.error(request, 'Please insert your data first.')
        return redirect('user_data')


def check_skill(request):
    try:
        usr = request.user
        dt = Data.objects.get(user=usr)
        dt_id = dt.id
        return redirect('skill', data=dt_id)
    except Data.DoesNotExist:
        messages.error(request, 'Please insert your data first.')
        return redirect('user_data')


def skill_delete(request, data=None, pk=None):
    if pk:
        sk = Skill.objects.get(pk=pk)
    else:
        sk = Skill()

    if sk:
        sk.delete()
        messages.warning(request, 'Skill deleted')
        return redirect('skill', data=data)
    else:
        form = SkillForm()
    return render(request, 'form_skill.html', {'form': form, })


def skill_edit(request, data=None, pk=None):
    myskill = Skill.objects.all().filter(data=data)
    if pk:
        sk = Skill.objects.get(pk=pk)
    else:
        sk = Skill()

    if 'save' in request.POST:
        if request.method == 'POST':
            form = SkillForm(request.POST, instance=sk)
            if form.is_valid():
                sk = form.save(commit=False)
                sk.data_id = data
                sk.save()
                messages.success(request, 'Skill edited')
                return redirect('skill', data=data)
    else:
        form = SkillForm(instance=sk)
    return render(request, 'skill_edit.html', {'form': form, 'mysk': myskill, })


# BerufForm
def experience_view(request, data=None):
    myexperience = Experience.objects.all().filter(data=data)
    if 'next' in request.POST:
        return redirect('education', data=data)
    elif 'add' in request.POST:
        if request.method == 'POST':
            form = ExperienceForm(request.POST)
            if form.is_valid():
                exp = form.save(commit=False)
                exp.data_id = data
                exp.save()
                messages.success(request, 'Experience saved')
                return redirect('experience', data=data)
    else:
        form = ExperienceForm()
    return render(request, 'form_experience.html', {'form': form, 'myexp': myexperience, })


def next_exp(request):
    try:
        usr = request.user
        dt = Data.objects.get(user=usr)
        dt_id = dt.id
        return redirect('education', data=dt_id)
    except Data.DoesNotExist:
        messages.error(request, 'Please insert your data first.')
        return redirect('user_data')


def check_exp(request):
    try:
        usr = request.user
        dt = Data.objects.get(user=usr)
        dt_id = dt.id
        return redirect('experience', data=dt_id)
    except Data.DoesNotExist:
        messages.error(request, 'Please insert your data first.')
        return redirect('user_data')


def experience_del(request, data=None, pk=None):
    if pk:
        exp = Experience.objects.get(pk=pk)
    else:
        exp = Experience()

    if exp:
        exp.delete()
        messages.warning(request, 'Experience deleted')
        return redirect('experience', data=data)
    else:
        form = SkillForm()
    return render(request, 'form_experience.html', {'form': form, })


def experience_edit(request, data=None, pk=None):
    myexperience = Experience.objects.all().filter(data=data)
    if pk:
        exp = Experience.objects.get(pk=pk)
    else:
        exp = Experience()

    if 'save' in request.POST:
        if request.method == 'POST':
            form = ExperienceForm(request.POST, instance=exp)
            if form.is_valid():
                exp = form.save(commit=False)
                exp.data_id = data
                exp.save()
                messages.success(request, 'Experience edited')
                return redirect('experience', data=data)
    else:
        form = ExperienceForm(instance=exp)
    return render(request, 'experience_edit.html', {'form': form, 'myexp': myexperience, })


# Ausbildung
def education_view(request, data=None):
    myeducation = Education.objects.all().filter(data=data)
    if 'add' in request.POST:
        if request.method == 'POST':
            form = EducationForm(request.POST)
            if form.is_valid():
                edu = form.save(commit=False)
                edu.data_id = data
                edu.save()
                messages.success(request, 'Education saved')
                return redirect('education', data=data)
    else:
        form = EducationForm()
    return render(request, 'form_education.html', {'form': form, 'myedu': myeducation, })


def education_del(request, data=None, pk=None):
    if pk:
        edu = Education.objects.get(pk=pk)
    else:
        edu = Education()

    if edu:
        edu.delete()
        messages.warning(request, 'Education deleted')
        return redirect('education', data=data)
    else:
        form = EducationForm()
    return render(request, 'form_education.html', {'form': form, })


def education_edit(request, data=None, pk=None):
    myeducation = Education.objects.all().filter(data=data)
    if pk:
        edu = Education.objects.get(pk=pk)
    else:
        edu = Education()

    if 'save' in request.POST:
        if request.method == 'POST':
            form = EducationForm(request.POST, instance=edu)
            if form.is_valid():
                edu = form.save(commit=False)
                edu.data_id = data
                edu.save()
                messages.success(request, 'Education edited')
                return redirect('education', data=data)
    else:
        form = EducationForm(instance=edu)
    return render(request, 'education_edit.html', {'form': form, 'myedu': myeducation, })


def check_edu(request):
    try:
        usr = request.user
        dt = Data.objects.get(user=usr)
        dt_id = dt.id
        return redirect('education', data=dt_id)
    except Data.DoesNotExist:
        messages.error(request, 'Please insert your data first.')
        return redirect('user_data')
