import requests

url = "https://microsoft-translator-text.p.rapidapi.com/translate"

querystring = {"to[0]":"en","api-version":"3.0","profanityAction":"NoAction","textType":"plain"}

payload = [{"Text": "kya haal hai"}]
headers = {
	"content-type": "application/json",
	"X-RapidAPI-Key": "cf7c61f9f8msh327f275682e3580p1f0e04jsn2120aeb1cd79",
	"X-RapidAPI-Host": "microsoft-translator-text.p.rapidapi.com"
}

response = requests.request("POST", url, json=payload, headers=headers, params=querystring)

print(response.text)