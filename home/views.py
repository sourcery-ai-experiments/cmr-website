from django.http import HttpResponse
from django.shortcuts import render


def credits(request):
    content = 'Martin Lanser'

    return HttpResponse(content, content_type='text/plain')


def news(request):
    data = {
        'news': [
            'First news item',
            'Second news item',
            'Third news item',
            'Fourth news item',
        ]
    }

    return render(request, 'news.html', data)
