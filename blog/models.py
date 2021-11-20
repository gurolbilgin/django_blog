from django.contrib.auth.models import User
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey


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
        return self.title


# Comment class is used by writing below as lowercase comment
#  this method is being used for reaching parent from a child

    def comment_count(self):
        return self.comment_set.all().count()
# PostView class is used by writing below as lowercase comment

    def view_count(self):
        return self.postview_set.all().count()

    def like_count(self):
        return self.like_set.all().count()

    def comments(self):
        return self.comment_set.all()


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    time_stamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    def __str__(self):
        return self.user.username


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class PostView(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE)
    post = models.ForeignKey(Post, on_delete=CASCADE)
    time_stamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
