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

from cvsite.views import get_home, get_cv_generator

from cvsite.views import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', get_home, name = 'home_page'),
    path('generate_cv/', get_cv_generator, name='genarate_template'),

    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('user/', get_user, name='list_user'),

    path('data/', data_view, name='user_data'),
    path('show_data/', show_data, name='show_data'),

    path('sprachen_view/<data>/', sprachen_view, name='sprachen'),

    path('kenntnisse_view/<data>/', kenntnisse_view, name='kenntnisse'),

    path('beruf_view/<data>/', beruf_view, name='beruf'),

    path('ausbildung_view/<data>/', ausbildung_view, name='ausbildung'),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
