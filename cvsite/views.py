from django.shortcuts import render

# Create your views here.
#home page
def get_home(request):
    return render(request, 'home.html', {'page_title' : 'Home CV Generator'})

def get_cv_generator(request):
    edu = ['template1_education.html', 'template1_education.html', 'template1_education.html']
    return render(request, 'generate_cv.html', {'page_title' : 'Generate your CV', 'edu' : edu})
