# from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
   # return HttpResponse("Hello World")
   return render(request, 'home.html')

def resources(request):
  #  return HttpResponse("Resources Page")
  return render(request, 'resources.html')

def arableague(request):
   return render(request, 'arableague.html')

def unhrc(request):
   return render(request, 'unhrc.html')

def unsc(request):
   return render(request, 'unsc.html')

def ecosoc(request):
   return render(request, 'ecosoc.html')

def secretariat(request):
   return render(request, 'secretariat.html')

def oc(request):
   return render(request, 'oc.html')

def register(request):
   return render(request, 'register.html')