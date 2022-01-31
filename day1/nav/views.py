from django.shortcuts import render
from django.http import HttpResponse
def nav(request):
    return render(request, 'nav.html')
def home(request,name):
    context={}
    context['NAME']=name
    return render(request, 'home.html',context)
def about_us (request):
    return render(request, 'about.html')
def contact_us(request):
    return render(request, 'contact.html')
