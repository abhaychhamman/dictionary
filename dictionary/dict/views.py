import imp
from django.shortcuts import render
from django.http import HttpResponse

from dict.models import Dictionary

# Create your views here.

def dictionary(request):
    if request.method=="POST":
        b = Dictionary(key=request.POST['key'],type=request.POST['type'],mean=request.POST['mean'],synonym=request.POST['synonym'] ,antonym=request.POST['antonym'],example=request.POST['example'])
        b.save()
        print("add successfully meaning")

    return render(request,"index.html")


def show_dict(request):
    data=Dictionary.objects.all().order_by('key').values()
    # print(data[0].example)
    context={
        'data':data
    }
    

    return render(request,"show_dictionary.html",context=context)


