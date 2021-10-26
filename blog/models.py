from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# print(User)


class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return str(self.author) + ' | ' + self.title
