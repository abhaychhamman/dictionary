import imp
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from dict.models import Dictionary
import json
# Create your views here.

def dictionary(request):
    if request.method=="POST":
        b = Dictionary(key=request.POST['key'],type=request.POST['type'],mean=request.POST['mean'],synonym=request.POST['synonym'] ,antonym=request.POST['antonym'],example=request.POST['example'])
        b.save()
        print("add successfully meaning")

    return render(request,"add_meaning.html")


def index(request):
     
    return render(request,"index.html")


def show_dict(request):
    data=Dictionary.objects.all().order_by('key').values()
    # print(data[0].example)
    context={
        'data':data
    }
    

    return render(request,"show_dictionary.html",context=context)

@csrf_exempt
def save_data(request):

    if request.method == "POST":

        print("hellowkdsjakg")
        res=Dictionary.objects.get(key=request.POST['key'])
         
        print(res.mean)
        result={
            "key":res.key,
            "mean":res.mean,
            "type":res.type,
            "synonym":res.synonym,
            "antonym":res.antonym,
            "example":res.example
        }
         
        

        return JsonResponse({'status': result})
    else:
        return JsonResponse({"status": 'fail'})


