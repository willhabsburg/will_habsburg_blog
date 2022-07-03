from django.shortcuts import render
from django.db.models import Count
from . import models

# Create your views here.
def home(request):
    """The Blog homepage"""
    # Get last 3 posts
    latest_posts = models.Post.objects.filter(status=models.Post.PUBLISHED).order_by('-published')[:3]
    # Get Topic list
    topics = {}
    #for post in latest_posts:
    #    if post.
    all_topics = models.Topic.objects.annotate(Count('blog_posts'))
    # Add as context variable "latest_posts"
    context = {
        'latest_posts': latest_posts,
        'all_topics': all_topics,
        }
    return render(request, 'blog/home.html', context)
