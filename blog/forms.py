from django import forms
from .models import Post


class Post_create_form(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", 'title_tag', 'content',
                  'image', 'status', 'category']
