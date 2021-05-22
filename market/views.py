from django.shortcuts import render
import requests
import json

def index(request):
    api_request = requests.get("https://cloud.iexapis.com/stable/stock/aapl/quote?token=pk_e0f0832eb6ed42508f905bb48f5791e0")
    try:
        api = json.loads(api_request.content)
    except Exception as e:
        api = "Error, data not loading"

    return render(request, 'index.html', {'api' : api})