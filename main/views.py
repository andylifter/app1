from django.http import HttpResponse
from django.shortcuts import render
from goods.models import Categories


def index(request):

    context: dict[str, str] = {
        'title': 'ИМПЕРИЯРЕМОНТА.РФ',
        'content': 'ИМПЕРИЯРЕМОНТА.РФ',
    }
    return render(request, 'main/index.html', context)


def about(request):
    context: dict[str, str] = {
        'title': 'О нас',
        'content': 'О нас', 
        'text_on_page': 'Тескст о том, какие мы хорошие и незаменимые'

    }
    return render(request, 'main/about.html', context)