 
import django


from django.contrib import admin
from django.urls import path

from dict.models import Dictionary
from .  import views


urlpatterns = [
    path("dict",views.dictionary,name="dictionary"),
    path("show_dict",views.show_dict,name="show_dict"),
    path("Home",views.index,name="show_dict"),
    path("save",views.save_data,name="save"),
    path("",views.index,name="index"),
]
