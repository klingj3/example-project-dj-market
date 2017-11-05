from django.contrib import messages
from django.urls import reverse
from django.views.generic import (DeleteView,
                                  DetailView,
                                  ListView,
                                  TemplateView)

from extra_views import (CreateWithInlinesView,
                         InlineFormSet,
                         UpdateWithInlinesView)
from itertools import chain
from market.apps.board.forms import (ImageHelper,
                                     PostForm,
                                     PostUpdateForm)
from market.apps.board.models import (Post,
                                      PostImage)
from market.apps.core.mixins import (CreateWithOwnerMixin,
                                     OwnerRequiredMixin,
                                     SellerRequiredMixin)

class ImagesInline(InlineFormSet):
    model = PostImage
    fields = ['image']
    extra = 5
    max_num = 5
    # can_delete = False


class PostCreateView(CreateWithOwnerMixin, SellerRequiredMixin, CreateWithInlinesView):
    model = Post
    inlines = [ImagesInline]
    form_class = PostForm
    template_name = 'board/post_form.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['image_helper'] = ImageHelper()
        return ctx

    def get_success_url(self):
        messages.success(self.request, 'Post created!', extra_tags='fa fa-check')
        return self.object.get_absolute_url()


class PostDeleteView(OwnerRequiredMixin, DeleteView):
    model = Post
    template_name = 'board/post_delete.html'

    def get_success_url(self):
        messages.success(self.request, 'Post deleted!', extra_tags='fa fa-check')
        return reverse('board:list')


class PostDetailView(DetailView):
    model = Post
    template_name = 'board/post_detail.html'


class PostListView(ListView):
    model = Post
    template_name = 'board/post_list.html'
    paginate_by = 8


class PostSearchView(ListView):
    model = Post
    template_name = 'board/post_search.html'
    paginate_by = 8

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            search_term = self.request.GET['q']
            search_term = search_term.replace('+', ' ')
            search_terms = search_term.split()
        except:
            search_term = ''
        if (search_term != ''):
            object_list_general = []
            object_list_intersection = self.model.objects.all()
            for term in search_terms:
                a = self.model.objects.filter(title__icontains=term)
                b = self.model.objects.filter(tags=term)
                object_list_intersection = list(set(object_list_intersection).intersection(set(chain(a, b))))
                object_list_general = list(set(chain(a, b, object_list_general)))
        else:
            object_list_general = self.model.objects.all()
        context['object_list_general'] = object_list_general
        return context

    def get_queryset(self):
        try:
            search_term = self.request.GET['q']
            search_term = search_term.replace('+', ' ')
            search_terms = search_term.split()
        except:
            search_term = ''
        if (search_term != ''):
            # First look for posts that matches exactly.
            # a = self.model.objects.filter(title__icontains=search_term)
            # b = self.model.objects.filter(tags=search_term)
            #object_list_explicit = list(set(chain(a, b)))

            # Then look for posts that contain one of the search words
            object_list_intersection = self.model.objects.all()
            for term in search_terms:
                a = self.model.objects.filter(title__icontains=term)
                b = self.model.objects.filter(tags=term)
                object_list_intersection = list(set(object_list_intersection).intersection(set(chain(a, b))))
        else:
            object_list_intersection = self.model.objects.all()
        return object_list_intersection

class PostUpdateView(OwnerRequiredMixin, UpdateWithInlinesView):
    model = Post
    inlines = [ImagesInline]
    form_class = PostUpdateForm
    template_name = 'board/post_update_form.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['image_helper'] = ImageHelper()
        return ctx

    def get_success_url(self):
        messages.success(self.request, 'Post updated!', extra_tags='fa fa-check')
        return self.object.get_absolute_url()


