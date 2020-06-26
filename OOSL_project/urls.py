"""OOSL_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from cvsite.views import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', get_home, name='home_page'),
    path('generate_cv/', get_cv_generator, name='genarate_template'),

    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('user/', get_user, name='list_user'),

    path('data/', data_view, name='user_data'),
    # path('data/<data>/', data_view, name='user_data'),
    path('show_data/', show_data, name='show_data'),

    path('language_view/<data>/', language_view, name='language'),
    path('language_delete/<data>/<pk>/', language_delete, name='language_del'),
    path('language_edit/<data>/<pk>/', language_edit, name='language_edit'),


    path('skill_view/<data>/', skill_view, name='skill'),
    path('skill_del/<data>/<pk>/', skill_delete, name='skill_delete'),
    path('skill_edit/<data>/<pk>/', skill_edit, name='skill_edit'),

    path('experience_view/<data>/', experience_view, name='experience'),
    path('experience_del/<data>/<pk>/', experience_del, name='experience_del'),
    path('experience_edit/<data>/<pk>/', experience_edit, name='experience_edit'),

    path('education_view/<data>/', education_view, name='education'),
    path('education_del/<data>/<pk>/', education_del, name='education_del'),
    path('education_edit/<data>/<pk>/', education_edit, name='education_edit'),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
