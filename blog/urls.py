from django.urls import path
from .views import ContentDetailView, HomeView

urlpatterns = [
    # class based url views here using as_view() is the thing needed to be watched for
    path('', HomeView.as_view(), name='home'),
    path('details/<int:pk>',  ContentDetailView.as_view(), name='details'),
]
