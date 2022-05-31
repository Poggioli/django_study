from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


# Create your views here.
def home(request: HttpRequest) -> HttpResponse:
    return HttpResponse(request.path)

def contact(request: HttpRequest) -> HttpResponse:
    return HttpResponse(request.path)

def about(request: HttpRequest) -> HttpResponse:
    return HttpResponse(request.path)

