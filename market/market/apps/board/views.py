from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import (CreateView,
                                  DeleteView,
                                  DetailView,
                                  ListView,
                                  TemplateView,
                                  UpdateView)

from market.apps.board.forms import PostForm
from market.apps.board.models import Post
from market.apps.core.mixins import CreateByUserMixin


class PostCreateView(CreateByUserMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'board/post_form.html'

    def get_success_url(self):
        return reverse('board:list')


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'board/post_delete.html'


class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'board/post_detail.html'


class PostListView(ListView):
    model = Post
    template_name = 'board/post_list.html'


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post


class TestView(TemplateView):
    template_name = 'base.html'
