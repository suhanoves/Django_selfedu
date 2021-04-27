from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request: HttpRequest) -> HttpResponse:
    return HttpResponse('Страница приложения Women')


def categories(request: HttpRequest) -> HttpResponse:
    return HttpResponse('<h1>Статьи по категориям</h1>')
