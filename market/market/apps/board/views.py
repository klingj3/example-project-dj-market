from django.contrib import messages
from django.shortcuts import render
from django.views.generic import TemplateView
from market.apps.board.models import Post

def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts,})

def post_detail(request, slug):
    post = Post.objects.get(slug=slug)
    return render(request, 'posts/post_detail.html', {'post':post})

class TestView(TemplateView):
    template_name = 'base.html'
