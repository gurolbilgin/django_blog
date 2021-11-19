from django.contrib import admin
from .models import Comment, Post, Category, Like, PostView

# Register your models here.

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Like)
admin.site.register(PostView)
admin.site.register(Comment)
