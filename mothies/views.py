from re import template

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


# Create your views here.
def home(request: HttpRequest) -> HttpResponse:
    return render(request=request, template_name='mothies/home.html', context={
        'name': 'João Pogiolli'
    })

def contact(request: HttpRequest) -> HttpResponse:
    return render(request=request, template_name='mothies/contact.html')

def about(request: HttpRequest) -> HttpResponse:
    return HttpResponse(request.path)

