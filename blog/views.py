from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post
# Create your views here.


# def home(request):
#     blogs = Post.objects.all()
#     return render(request, 'home.html', {'blogs': blogs})


class HomeView(ListView):
    model = Post
    template_name = 'home.html'


class ContentDetailView(DetailView):
    model = Post
    template_name = "details.html"


class AddBlogView(CreateView):
    model = Post
    template_name = 'add_blog.html'
    fields = '__all__'
