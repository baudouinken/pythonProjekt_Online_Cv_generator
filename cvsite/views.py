from django.shortcuts import render

# Create your views here.
#home page
def get_home(request):
    return render(request, 'home.html', {'page_title': 'Home CV Generator'})

def get_cv_generator(request):
    ids = ['Photo', 'Name', 'Adress', 'Skills', 'About', 'Experience', 'Education']
    templates = {"Photo": ['template1_photo.html', 'template1_photo.html', 'template1_photo.html'],
                 "Name": ['template1_name.html', 'template1_name.html', 'template1_name.html'],
                 "Adress": ['template1_adress.html', 'template1_adress.html', 'template1_adress.html'],
                 "Skills": ['template1_skills.html', 'template1_skills.html', 'template1_skills.html'],
                 "About": ['template1_about.html', 'template1_about.html', 'template1_about.html'],
                 "Experience": ['template1_experience.html', 'template1_experience.html', 'template1_experience.html'],
                 "Education": ['template1_education.html', 'template1_education.html', 'template1_education.html']
                 }
    return render(request, 'generate_cv.html', {'page_title': 'Generate your CV', 'ids': ids, 'templates': templates})
