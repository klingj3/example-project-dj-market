from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import (CreateView,
                                  DeleteView,
                                  DetailView,
                                  ListView,
                                  TemplateView,
                                  UpdateView)

from extra_views import (CreateWithInlinesView,
                         InlineFormSet)

from market.apps.board.forms import PostForm
from market.apps.board.models import (Post,
                                      PostImage)
from market.apps.core.mixins import (CreateWithOwnerMixin,
                                     OwnerRequiredMixin)


# class PostCreateView(CreateWithOwnerMixin, CreateView):
#     model = Post
#     form_class = PostForm
#     template_name = 'board/post_form.html'
#
#     def get_success_url(self):
#         messages.success(self.request, 'Posting successfully created!', extra_tags='fa fa-check')
#         return reverse('board:list')


class ImagesInline(InlineFormSet):
    model = PostImage
    fields = ['image']
    # extra = 5
    max_num = 2


class PostCreateView(CreateWithOwnerMixin, CreateWithInlinesView):
    model = Post
    form_class = PostForm
    template_name = 'board/post_form.html'
    inlines = [ImagesInline]

    def get_success_url(self):
        return self.object.get_absolute_url()


class PostDeleteView(OwnerRequiredMixin, DeleteView):
    model = Post
    template_name = 'board/post_delete.html'


class PostDetailView(DetailView):
    model = Post
    template_name = 'board/post_detail.html'


class PostListView(ListView):
    model = Post
    template_name = 'board/post_list.html'
    paginate_by = 8


class PostUpdateView(OwnerRequiredMixin, UpdateView):
    model = Post


class TestView(TemplateView):
    template_name = 'base.html'
