from django.contrib.auth.models import User
from django.db import models


# Create your models here.

# print(User)

STATUS = [('Draft', 'Draft'), ('Publish', 'Publish')]

CATEGORY = [('Full-Stack', 'Full-Stack'), ('Front-end',
                                           'Front-end'), ('Back-end', 'Back-end')]


class Post(models.Model):
    title = models.CharField(max_length=200)
    title_tag = models.CharField(
        max_length=30, default='A Blogpost!!!', blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    image = models.ImageField(
        upload_to='blog_pictures/', default='full-stack-developer.png', blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    status = models.CharField(max_length=10, choices=STATUS, default="Draft")

    category = models.CharField(
        max_length=10, choices=CATEGORY, default='Full-Stack')

    def __str__(self):
        return str(self.author) + ' | ' + self.title
