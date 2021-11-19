from django import forms
from django.db.models import fields
from .models import Category, Post, Comment


class PostForm(forms.ModelForm):
    status = forms.ChoiceField(choices=Post.STATUS)
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(), empty_label='Select')

    class Meta:
        model = Post
        fields = ["title", 'content',
                  'image', 'status', 'category']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
