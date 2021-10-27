from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime


# Create your models here.

# print(User)


class Post(models.Model):
    title = models.CharField(max_length=200)
    title_tag = models.CharField(
        max_length=30, default='Awesome Blogpost!!!', blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    image = models.ImageField(
        upload_to='blog_pictures/', default='full-stack-developer.png', blank=True)
    date = models.DateTimeField(default=datetime.now, blank=True)
    # last_update_date = models.DateField()
    STATUS = (('Draft'), ('Publish'))

    models.CharField(max_length=50, choices=STATUS, default="Draft")

    def __str__(self):
        return str(self.author) + ' | ' + self.title

    def get_absolute_url(self):
        return reverse("details", args=str(self.id))


# kwargs = {"pk": self.pk}
