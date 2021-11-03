from django.http import request
from django.shortcuts import render, redirect
from .models import Post
from .forms import Post_create_form
# Create your views here.

# SHOW DASHBOARD


def home(request):
    blogs = Post.objects.all()
    return render(request, 'blog/home.html', {'blogs': blogs})


# ADD BLOG

def add_blog(request):
    form = Post_create_form()
    print(request)
    if request.method == 'POST':
        form = Post_create_form(request.POST, request.FILES)
        if form.is_valid():
            # post creates form and waits and does not send to the database
            #  we are waiting until creating the user before submitting the form  we are not just asking the users their name we are just craeting their name in the database automatically
            post = form.save(commit=False)
            post.author = request.user

            form.save()
            return redirect('home')

    return render(request, 'add_blog.html', {'form': form})


# CONTENT DETAIL

def detailed_blog(request, id):
    blog = Post.objects.get(id=id)
    return render(request, 'details.html', {'blog': blog})


# UPDATE BLOG

def update_blog(request, id):
    blog = Post.objects.get(id=id)

    form = Post_create_form(instance=blog)

    if request.method == 'POST':
        form = Post_create_form(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {
        'blog': blog, 'form': form
    }

    return render(request, 'update.html', context)

    # DELETE BLOG


def delete_blog(request, id):
    blog = Post.objects.get(id=id)

    if request.method == 'POST':
        blog.delete()
        return redirect('home')

    return render(request, 'delete.html', {'blog': blog})
