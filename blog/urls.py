from django.urls import path
from .views import delete_blog, home, add_blog, detailed_blog, update_blog

urlpatterns = [
    # class based url views here using as_view() is the thing needed to be watched for
    path('', home, name='home'),
    # path('add_blog/',  add_blog, name='add_blog'),
    # path('details/<int:id>', detailed_blog, name='details'),
    # path('update/<int:id>', update_blog, name='update'),
    # path('delete/<int:id>', delete_blog, name='delete'),
]
