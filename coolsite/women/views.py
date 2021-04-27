from django.http import HttpRequest, HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render

from women.models import *

menu = ["О сайте", "Добавить статью", "Обратная связь", "Войти"]


# Create your views here.
def index(request: HttpRequest) -> HttpResponse:
    posts = Women.objects.all()
    return render(request, 'women/index.html', {'posts': posts, 'menu': menu, 'title': 'Главная страница'})


def about(request: HttpRequest) -> HttpResponse:
    return render(request, 'women/index.html', {'menu': menu, 'title': 'О сайте'})


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
