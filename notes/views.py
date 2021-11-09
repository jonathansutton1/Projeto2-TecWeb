from django.shortcuts import render, redirect
from .models import Fin
import requests
import json
def acha_tudo(simbolo):
    url = "https://alpha-vantage.p.rapidapi.com/query"
    querystring = {"function":"GLOBAL_QUOTE","symbol":f"{simbolo}","datatype":"json"}
    headers = {
        'x-rapidapi-host': "alpha-vantage.p.rapidapi.com",
        'x-rapidapi-key': "a1f75e85bemshc92ab3c51eb0c23p1e6aeejsnb8824cdc997c"
        }
    response = requests.request("GET", url, headers=headers, params=querystring)
    todos = json.loads(response.text)
    todos == response.json()
    symbol= todos['Global Quote']['01. symbol']
    value = todos['Global Quote']['05. price']
    date = todos['Global Quote']['07. latest trading day']
    return symbol, value, date
def index(request):
    if request.method == 'POST':
        symbol = request.POST.get('symbol')
        symbol, value, date = acha_tudo(symbol)
        fin = Fin()
        fin.symbol = symbol
        fin.value = value
        fin.date = date
        fin.save()
        return redirect('index')
    else:
        last_note = Fin.objects.last()
        notes = Fin.objects.all()
        return render(request, 'notes/index.html', {'note': last_note, 'notes': notes})
