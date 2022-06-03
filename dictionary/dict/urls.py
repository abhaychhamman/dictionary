import imp
from unicodedata import name
import django


from django.contrib import admin
from django.urls import path

from dict.models import Dictionary
from .  import views


urlpatterns = [
    path("dict",views.dictionary,name="dictionary"),
    path("show_dict",views.show_dict,name="show_dict"),
]
