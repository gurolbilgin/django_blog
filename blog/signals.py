# for slug before recording
from django.db.models.signals import pre_save
# for before saving post wait and do this...
from django.dispatch import reciever
# slugify seperates the url with dashes '-'
from django.template.defaultfilters import slugify
from .models import Post


@reciever(pre_save, sender=Post)
def pre_save_create_slug(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = slugify(
            instance.author.username + " " + instance.title)
