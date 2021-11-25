from django.urls import path
from .views import home, like,  post_create, post_delete, post_detail, post_update

urlpatterns = [

    path('', home, name='home'),
    path('create/',  post_create, name='create'),
    path('<str:slug>/', post_detail, name='details'),
    path('<str:slug>/update/', post_update, name='update'),
    path('<str:slug>/delete', post_delete, name='delete'),
    path('<str:slug>/like', like, name='like'),
]
