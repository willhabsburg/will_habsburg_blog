# will_habsburg_blog/views.py

from django.http import HttpResponse


def index(request):
    return HttpResponse('Hello world!')