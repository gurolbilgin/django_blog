from django.http import request
from django.shortcuts import get_object_or_404, render, redirect
from .models import Like, Post
from .forms import CommentForm, PostForm
# Create your views here.


# RENDER DASHBOARD
def home(request):
    # only published posts can be seen on the dashboard
    blogs = Post.objects.filter(status='p')
    return render(request, 'blog/home.html', {'blogs': blogs})


# ADD BLOG
def post_create(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            # post creates form and waits and does not send to the database
            #  we are waiting until creating the user before submitting the form  we are not just asking the users their name we are just craeting their name in the database automatically
            post = form.save(commit=False)
            post.author = request.user
            # then
            post.save()
            return redirect('home')

    return render(request, 'post_create.html', {'form': form})


# CONTENT DETAIL
def post_detail(request, slug):
    form = CommentForm()
    blog = get_object_or_404(slug=slug)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = blog
            comment.save()
            return redirect('post_detail', slug=slug)

    return render(request, 'post_detail.html', {'blog': blog, 'form': form})


# UPDATE BLOG
def post_update(request, slug):
    blog = get_object_or_404(Post, slug=slug)
    form = Post(request.POST or None, request.FILES or None, instance=blog)
    if form.is_valid():
        form.save()
        return redirect('home')

    context = {
        'blog': blog, 'form': form
    }
    return render(request, 'post_update.html', context)


# DELETE BLOG
def post_delete(request, slug):
    blog = get_object_or_404(Post, slug=slug)
    if request.method == 'POST':
        blog.delete()
        return redirect('home')
    return render(request, 'post_delete.html', {'blog': blog})

# LIKE COUNT


def like(request, slug):
    if request.method == 'POST':
        obj = get_object_or_404(Post, slug=slug)
        like_qs = Like.objects.filter(user=request.user, post=obj)
        if like_qs.exists():
            like_qs[0].delete()
        else:
            Like.objects.create(user=request.user, post=obj)
        return redirect('post_detail', slug=slug)
