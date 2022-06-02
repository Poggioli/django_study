from re import template

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


# Create your views here.
def home(request: HttpRequest) -> HttpResponse:
    return render(request=request, template_name='mothies/pages/home.html', context={
        'name': 'João Pogiolli'
    })
