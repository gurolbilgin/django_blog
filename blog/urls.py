from django.urls import path
from .views import ContentDetailView, HomeView, AddBlogView

urlpatterns = [
    # class based url views here using as_view() is the thing needed to be watched for
    path('', HomeView.as_view(), name='home'),
    path('details/<int:pk>',  ContentDetailView.as_view(), name='details'),
    path('add_blog/',  AddBlogView.as_view(), name='add_blog'),
]
