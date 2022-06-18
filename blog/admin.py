from django.contrib import admin
from . import models
from blog.models import Comment


class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'created',
    )
    list_filter = (
        'name',
        'approved',
    )
    search_fields = (
        'text',
        'name__username',
        'name__first_name',
        'name__last_name',
    )

class CommentInline(admin.TabularInline):
    model = Comment
    fk_name = "post"

class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'created',
        'updated',
    )
    search_fields = (
        'title',
        'author__username',
        'author__first_name',
        'author__last_name',
    )
    list_filter = (
        'status',
        'topics',
    )
    prepopulated_fields = {'slug': ('title',)}
    inlines = [CommentInline,]

class TopicAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'slug',
    )
    list_filter = (
        'name',
    )
    prepopulated_fields = {'slug': ('name',)}

class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'created',
    )
    list_filter = (
        'name',
        'approved',
    )
    search_fields = (
        'text',
        'name__username',
        'name__first_name',
        'name__last_name',
    )


admin.site.register(models.Post, PostAdmin)
admin.site.register(models.Topic, TopicAdmin)
admin.site.register(models.Comment, CommentAdmin)
