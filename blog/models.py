from django.db import models
from django.conf import settings

class Topic(models.Model):
    """
    Represents a topic for a blog post
    """

    name = models.CharField(
        max_length = 50,
        unique = True,
    )
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']



class Post(models.Model):
    """
    Represents a blog post
    """

    DRAFT = 'draft'
    PUBLISHED = 'published'
    STATUS_CHOICES = [
        (DRAFT, 'Draft'),
        (PUBLISHED, 'Published')
    ]

    title = models.CharField(
        max_length=255,
        null=False,
    )
    content = models.TextField()
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name='blog_posts',
        null=False,
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default=DRAFT,
        help_text='Set to "published" to make this post publicly visible',
        null=False,
    )
    published = models.DateTimeField(
        null=True,
        blank=True,
        help_text='The date and time this article was published',
    )
    slug = models.SlugField(
        null=False,
        help_text='The date and time this article was published',
        unique_for_date='published',
    )
    topics = models.ManyToManyField(
        Topic,
        related_name = 'blog_posts',
    )

    class Meta:
        ordering = ['-created']
        
    def __str__(self):
        return self.title

class Comment(models.Model):
    """
    A model to represent blog post comments
    """
    APPROVED = 'approved'
    PENDING = 'pending'
    DENIED = 'denied'
    APPROVED_CHOICES = [
        (APPROVED, 'Approved'),
        (PENDING, 'Pending'),
        (DENIED, 'Denied')
    ]

    post = models.ForeignKey(
        Post,
        on_delete=models.PROTECT,
        related_name='comments',
        null=False,
    )
    name = models.CharField(
        max_length = 100,
        null = False,
    )
    """models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name='blog_posts',
        null=False,
    )
    """
    email = models.CharField(
        max_length=255,
        null=False,
    )
    text = models.TextField(
        max_length=2048,
        null=False,
    )
    approved = models.CharField(
        max_length=10,
        choices=APPROVED_CHOICES,
        default=PENDING,
        help_text='Set to "Approved" to make this comment visible to users',
        null=False,
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created']