from multiprocessing import context
from django.shortcuts import render

# Create your views here.

def homepage(request):
    context= {
        'title': ''
    }
    return render(request, 'general/index.html',)

def about(request):
    return render(request, 'general/about.html')

def contact(request):
    return render(request, 'general/contact.html')

def company(request):
    return render(request, 'general/company.html')

def furnitures(request):
    return render(request, 'general/furnitures.html')
