   

from django.shortcuts import render
from django.http import JsonResponse
import requests
import json

# Create your views here.

def translate(request):


    if request.method=='POST':
    

        if request.POST['target_language']== request.POST['source_language']:
            return render(request,"Translate.html",context={"message":"please select different target Lanugage "})


        url = "https://google-translate1.p.rapidapi.com/language/translate/v2"

        payload = f"q={request.POST['ex']}&target={request.POST['target_language']}&source={request.POST['source_language']}"
        headers = {
	"content-type": "application/x-www-form-urlencoded",
	"Accept-Encoding": "application/gzip",
	"X-RapidAPI-Key": "b074fc0f12mshde9f23386b948b0p159763jsn0a3570621e18",
	"X-RapidAPI-Host": "google-translate1.p.rapidapi.com"
}
        
        response = requests.request("POST", url, data=payload, headers=headers)

        print(response.text)
        return render(request,"Translate.html",context={"result":json.loads(response.text)['data']['translations'][0]['translatedText']})
  
    return render(request,"Translate.html")
    