"""proj_english URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('words-list', views.words_list),
    path('words-add', views.words_add),
    path('words-send', views.words_send),
    path('words-learn', views.words_learn),
    path('words-delete', views.words_delete),
    path('theory-list', views.theory_list),
    path('theory-details', views.theory_details),
    path('tests-list', views.tests_list),
    path('tests-details', views.tests_details),
]
