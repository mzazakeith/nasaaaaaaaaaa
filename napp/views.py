from django.shortcuts import render, redirect, get_object_or_404
import requests
from django.http import JsonResponse
from nasa import settings


def index(request):
    endpoint = 'https://api.nasa.gov/planetary/apod?api_key={api_key}'
    url = endpoint.format(api_key=settings.NASA_KEY)
    response = requests.get(url)
    results = response.json()
    print(results)
    return render(request, 'index.html')

