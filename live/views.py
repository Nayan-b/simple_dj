# import render and request from django
from django.shortcuts import render, HttpResponse, redirect


# create a view for the live page
def index(request):
    return render(request, 'basic.html')

def contact(request):
    return render(request, 'contact.html')
