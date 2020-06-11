from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
#home page
def get_home(request):
    return render(request, 'home.html', {'page_title': 'Home CV Generator'})


def get_cv_generator(request):
    ids = ['Photo', 'Name', 'Adress', 'Skills', 'About', 'Experience', 'Education', 'Language']
    templates = {"Photo": ['template1/template1_photo.html', 'template2/template2_photo.html', 'template3/template3_photo.html', 'template4/template4_photo.html'],
                 "Name": ['template1/template1_name.html', 'template2/template2_name.html', 'template3/template3_name.html', 'template4/template4_name.html'],
                 "Adress": ['template1/template1_adress.html', 'template2/template2_adress.html', 'template3/template3_adress.html', 'template4/template4_adress.html'],
                 "Skills": ['template1/template1_skills.html', 'template2/template2_skills.html', 'template3/template3_skills.html', 'template4/template4_skills.html'],
                 "About": ['template1/template1_about.html', 'template2/template2_about.html', 'template3/template3_about.html', 'template4/template4_about.html'],
                 "Experience": ['template1/template1_experience.html', 'template2/template2_experience.html', 'template3/template3_experience.html', 'template4/template4_experience.html'],
                 "Education": ['template1/template1_education.html', 'template2/template2_education.html', 'template3/template3_education.html', 'template4/template4_education.html'],
                 "Language": ['template1/template1_language.html', 'template2/template2_language.html', 'template3/template3_language.html', 'template4/template4_language.html']
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
            return redirect('sprachen', data=data_id)
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
def sprachen_view(request, data=None):
    if 'next' in request.POST:
        if request.method == 'POST':
            form = SprachenForm(request.POST)
            if form.is_valid():
                sp = form.save(commit=False)
                sp.data_id = data
                sp.save()
                return redirect('kenntnisse', data=data)
    elif 'add' in request.POST:
        if request.method == 'POST':
            form = SprachenForm(request.POST)
            if form.is_valid():
                sp = form.save(commit=False)
                sp.data_id = data
                sp.save()
                return redirect('sprachen', data=data)
    else:
        form = SprachenForm()
    return render(request, 'form_sprachen.html', {'form': form})


# Kenntnisse
def kenntnisse_view(request, data=None):
    if 'next' in request.POST:
        if request.method == 'POST':
            form = KenntnisseForm(request.POST)
            if form.is_valid():
                kt = form.save(commit=False)
                kt.data_id = data
                kt.save()
                return redirect('beruf', data=data)
    elif 'add' in request.POST:
        if request.method == 'POST':
            form = KenntnisseForm(request.POST)
            if form.is_valid():
                kt = form.save(commit=False)
                kt.data_id = data
                kt.save()
                return redirect('kenntnisse', data=data)
    else:
        form = KenntnisseForm()
    return render(request, 'form_kentnisse.html', {'form': form})


# BerufForm
def beruf_view(request, data=None):
    if 'next' in request.POST:
        if request.method == 'POST':
            form = BerufForm(request.POST)
            if form.is_valid():
                be = form.save(commit=False)
                be.data_id = data
                be.save()
                return redirect('ausbildung', data=data)
    elif 'add' in request.POST:
        if request.method == 'POST':
            form = BerufForm(request.POST)
            if form.is_valid():
                be = form.save(commit=False)
                be.data_id = data
                be.save()
                return redirect('kenntnisse', data=data)
    else:
        form = BerufForm()
    return render(request, 'form_beruf.html', {'form': form})


# Ausbildung
def ausbildung_view(request, data=None):
    if 'next' in request.POST:
        if request.method == 'POST':
            form = AusbildungForm(request.POST)
            if form.is_valid():
                au = form.save(commit=False)
                au.data_id = data
                au.save()
                return redirect('list_user')
    elif 'add' in request.POST:
        if request.method == 'POST':
            form = AusbildungForm(request.POST)
            if form.is_valid():
                au = form.save(commit=False)
                au.data_id = data
                au.save()
                return redirect('ausbildung', data=data)
    else:
        form = AusbildungForm()
    return render(request, 'form_ausbildung.html', {'form': form})
