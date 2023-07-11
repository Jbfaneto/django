from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, 'recipes/home.html')
    
def contatos(request):
    return HttpResponse('contatos')

def sobre(request):
    return HttpResponse('sobre')
    