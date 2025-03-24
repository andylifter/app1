from django.http import HttpResponse
from django.shortcuts import render
from goods.models import Categories
# Create your views here.

def index(request):

    categories = Categories.objects.all()

    context: dict[str, str] = {
        'title': 'ИМПЕРИЯРЕМОНТА.РФ',
        'content': 'ИМПЕРИЯРЕМОНТА.РФ',
        'categories': categories
    }

    return render(request, 'main/index.html', context)


def about(request):
    context: dict[str, str] = {
        'title': 'О нас',
        'content': 'О нас', 
        'text_on_page': 'Тескст о том, какие мы хорошие и незаменимые'

    }
    return render(request, 'main/about.html', context)