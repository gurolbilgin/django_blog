# for slug before recording
import django
from django.db.models.signals import pre_save
# before saving post wait and do this...
from django.dispatch import reciever
# slugify seperates the url with dashes '-'
from django.template.defaultfilters import slugify
from .models import Post
# import utils for unique id
from .utils import get_random_code


@reciever(pre_save, sender=Post)
def pre_save_create_slug(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = slugify(
            instance.title + ' ' + get_random_code())


django.VERSION
