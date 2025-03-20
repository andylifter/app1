from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.

def index(request):
    context: dict[str, str] = {
        'title': 'Home',
        'content': 'Главная страница магазина - HOME',
        'list': ['first', 'second', [1, 2, 4], ('a', 'b', 'c')], 
        'dict': {'first': 1}, 
        'is_autenticated': False 
    }
    return render(request, 'main/index.html', context)


def about(request):
    return HttpResponse('About page')