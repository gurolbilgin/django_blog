from django.contrib.auth.models import User
from django.db import models


# the path function for media files
# 0 represents the author's id folder, and 1 represents the picture represents the author uploads
def user_directory(instance, filename):
    return "blog/{0}/{1}".format(instance.author.id, filename)


# Only admin can create a new category
class Category(models.Model):
    name = models.CharField(max_length=100)
    #  !!! TEST It later for whether it's necessary for the plural Categoty or not
    # class Meta:
    #     verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Post(models.Model):
    STATUS = [('d', 'Draft'), ('p', 'Publish')]

    title = models.CharField(max_length=200)
    title_tag = models.CharField(
        max_length=30, default='A Blogpost!!!', blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    image = models.ImageField(
        upload_to=user_directory, default='full-stack-developer.png', blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    status = models.CharField(max_length=10, choices=STATUS, default="d")

    category = models.ForeignKey(Category, on_delete=models.PROTECT)

    slug = models.SlugField(blank=True, unique=True)

    def __str__(self):
        return str(self.author) + ' | ' + self.title
