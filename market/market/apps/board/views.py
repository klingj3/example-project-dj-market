from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from market.apps.board.models import Post
from market.apps.board.forms import PostForm

def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts,})

def edit_post(request, slug):
    post = Post.objects.get(slug=slug)
    form_class = PostForm

    # If we reach this point from a submitted form
    if request.method == 'POST':
        # Take data from the submitted form and apply it here.
        form = form_class(data=request.POST, instance=post)
        if form.is_valid():
            # Save if valid.
            form.save()
            return redirect('post_detail', slug=post.slug)
    # Otherwise create the form
    else:
        form = form_class(instance=post)
    return render(request, 'posts/edit_post.html', {'post':post, 'form':form,})

def post_detail(request, slug):
    post = Post.objects.get(slug=slug)
    return render(request, 'posts/post_detail.html', {'post':post})

class TestView(TemplateView):
    template_name = 'base.html'
