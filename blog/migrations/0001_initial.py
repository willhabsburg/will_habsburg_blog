# Generated by Django 4.0.4 on 2022-06-18 17:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='draft', help_text='Set to "published" to make this post publicly visible', max_length=10)),
                ('published', models.DateTimeField(blank=True, help_text='The date and time this article was published', null=True)),
                ('slug', models.SlugField(help_text='The date and time this article was published', unique_for_date='published')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='blog_posts', to=settings.AUTH_USER_MODEL)),
                ('topics', models.ManyToManyField(related_name='blog_posts', to='blog.topic')),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=255)),
                ('text', models.TextField(max_length=2048)),
                ('approved', models.CharField(choices=[('approved', 'Approved'), ('pending', 'Pending'), ('denied', 'Denied')], default='pending', help_text='Set to "Approved" to make this comment visible to users', max_length=10)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='comments', to='blog.post')),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]
