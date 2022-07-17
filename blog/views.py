from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from django.views.generic import DetailView
from . import models

class HomeView(TemplateView):
    """The Blog homepage"""
    template_name = 'blog/home.html'

    def get_context_data(self, **kwargs):
        # Get the parent context
        context = super().get_context_data(**kwargs)
        
        # Get last 3 posts
        latest_posts = models.Post.objects.filter(status=models.Post.PUBLISHED).order_by('-published')[:3]

        # Update the context with our context variables
        context.update({
            'latest_posts': latest_posts,
        })

        return context

class AboutView(TemplateView):
    """Renders the About page view"""
    template_name = 'blog/about.html'

class PostListView(ListView):
    model = models.Post
    context_object_name = 'posts'
    queryset = models.Post.objects.filter(status=models.Post.PUBLISHED).order_by('-published')

class PostDetailView(DetailView):
    model = models.Post

    def get_queryset(self):
        # If this is a `pk` lookup, use default queryset
        if 'pk' in self.kwargs:
            return super().get_queryset()

        # Otherwise, filter on the published date
        queryset = super().get_queryset().filter(status=models.Post.PUBLISHED)
        return queryset.filter(
            published__year=self.kwargs['year'],
            published__month=self.kwargs['month'],
            published__day=self.kwargs['day'],
        )

class TopicListView(ListView):
    model = models.Topic
    context_object_name = 'topics'
    queryset = models.Topic.objects.filter(blog_posts__status=models.Post.PUBLISHED).distinct().order_by('name')

class TopicDetailView(DetailView):
    model = models.Topic
    def get_queryset(self):
        return super().get_queryset().order_by('blog_posts__published')
