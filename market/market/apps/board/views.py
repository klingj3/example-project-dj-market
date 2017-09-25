from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.template.defaultfilters import slugify
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from market.apps.board.models import Post
from market.apps.board.forms import PostForm


def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts,})

def create_post(request):
    form_class = PostForm

    # If we're coming here from an existing form
    if request.method == 'POST':
        # Apply data from the old form and apply to the new
        form = form_class(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.slug = slugify(post.title)
            post.save()
            return redirect('post_detail', slug=post.slug)
    else:
        form = form_class()

    return render(request, 'posts/create_post.html', {'form':form,})

@login_required
def edit_post(request, slug):
    post = Post.objects.get(slug=slug)

    if post.user != request.user:
        raise Http404

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
