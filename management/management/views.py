from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def fname2(request, nome):
    return render(request, 'pessoa.html')