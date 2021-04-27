from django.http import HttpRequest, HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect


# Create your views here.
def index(request: HttpRequest) -> HttpResponse:
    return HttpResponse('Страница приложения Women')


def categories(request: HttpRequest, catid: int) -> HttpResponse:
    if request.POST:
        print(request.POST)

    return HttpResponse(f"<h1>Статьи по категориям</h1><p>{catid}</p>")


def archive(request: HttpRequest, year: str) -> HttpResponse:
    if int(year) > 2020:
        raise Http404()

    return HttpResponse(f"<h1>Архив по годам</h1><p>{year}</p>")


def pageNotFound(request: HttpRequest, exception) -> HttpResponseNotFound:
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
