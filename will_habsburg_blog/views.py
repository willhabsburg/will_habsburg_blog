"""
Views code for will_habsburg_blog
"""
# will_habsburg_blog/views.py

from django.http import HttpResponse


def index(request):
    """ This returns a simple hello world """
    return HttpResponse('Hello world!')
