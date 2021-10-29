from django.http import request
from django.shortcuts import render, redirect
from .models import Post
from .forms import Post_create_form
# Create your views here.

# SHOW DASHBOARD


def home(request):
    blogs = Post.objects.all()
    return render(request, 'home.html', {'blogs': blogs})


# ADD BLOG

def add_blog(request):
    form = Post_create_form()
    print(request)
    if request.method == 'POST':
        form = Post_create_form(request.POST, request.FILES)
        if form.is_valid():
            # post creates form and waits and does not send to database
            post = form.save(commit=False)
            post.author = request.user
            form.save()
            return redirect('home')

    return render(request, 'add_blog.html', {'form': form})


# CONTENT DETAIL

def detailed_blog(request, id):
    blog = Post.objects.all(id=id)
    return render(request, 'blog/details.html', {'blog': blog})


# UPDATE BLOG

def update_blog(request, id):
    blog = Post.objects.all(id=id)
    post = Post

    if request.method == 'POST':
        post = Post(request.POST, request.FILES)
        if post.is_valid():
            post.save()
            return redirect('home')

    context = {
        'blog': blog, 'post': post
    }

    return render(request, 'blog/update.html', context)

    # DELETE BLOG

    # def delete_blog(request, id):
