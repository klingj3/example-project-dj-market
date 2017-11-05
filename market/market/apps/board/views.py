from django.contrib import messages
from django.urls import reverse
from django.views.generic import (DeleteView,
                                  DetailView,
                                  ListView,
                                  TemplateView)

from extra_views import (CreateWithInlinesView,
                         InlineFormSet,
                         UpdateWithInlinesView)
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
        context = super().get_context_data(**kwargs)
        context['image_helper'] = ImageHelper()
        return context

    def get_success_url(self):
        messages.success(self.request, 'Post created!', extra_tags='fa fa-check')
        return self.object.get_absolute_url()


class PostDeleteView(OwnerRequiredMixin, DeleteView):
    model = Post
    # TODO: Can this use a form?
    template_name = 'board/post_confirm_delete.html'

    def get_success_url(self):
        messages.success(self.request, 'Post deleted!', extra_tags='fa fa-check')
        return reverse('board:list')


class PostDetailView(DetailView):
    model = Post
    template_name = 'board/post_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Get most similar posts by tags
        # TODO: Also weight by distance
        # TODO: Search for posts with query based on this one
        context['similar_posts'] = Post.objects.all()[:4]
        return context


class PostListView(ListView):
    model = Post
    template_name = 'board/post_list.html'
    paginate_by = 8


class PostSearchView(ListView):
    model = Post
    template_name = 'board/post_list.html'
    # paginate_by = 8

    # def get_queryset(self):
    #     # TODO: Pre-process search query to
    #     qs = self.model.objects.search()
    #
    #     # Sort by specified rule
    #     sort_rule = self.request.GET.get('sort')
    #     if sort_rule:
    #         if sort_rule == 'date-newest':
    #             qs = qs.order_by('modified')
    #         elif sort_rule == 'date-oldest':
    #             qs = qs.order_by('-modified')
    #         elif sort_rule == 'price-lowest':
    #             qs = qs.order_by('price')
    #         elif sort_rule == 'price-highest':
    #             qs = qs.order_by('-price')
    #
    #     return qs


# TODO: No listview, only search. Show all if no query
# class PostSearchView(ListView):
#     model = Post
#     template_name = 'board/post_search.html'
#     paginate_by = 8
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         try:
#             search_term = self.request.GET['q']
#             search_term = search_term.replace('+', ' ')
#             search_terms = search_term.split()
#         except:
#             search_term = ''
#         context['past_query'] = search_term
#
#         try:
#             sort_type = self.request.GET['sort']
#         except:
#             sort_type = 'modified'
#
#         if (search_term != ''):
#             object_list_general = []
#             for term in search_terms:
#                 a = self.model.objects.filter(title__icontains=term)
#                 b = self.model.objects.filter(tags=term)
#                 object_list_general = list(set(chain(a, b, object_list_general)))
#         else:
#             object_list_general = self.model.objects.order_by(sort_type)
#         context['object_list_general'] = object_list_general
#
#         return context
#
#     def get_queryset(self):
#         try:
#             sort_type = self.request.GET['sort']
#         except:
#             sort_type = 'modified'
#         try:
#             search_term = self.request.GET['q']
#             search_term = search_term.replace('+', ' ')
#             search_terms = search_term.split()
#         except:
#             search_term = ''
#         if (search_term != ''):
#             object_list_intersection = self.model.objects.order_by(sort_type)
#             for term in search_terms:
#                 a = self.model.objects.filter(title__icontains=term)
#                 b = self.model.objects.filter(tags=term)
#                 object_list_intersection = list(set(object_list_intersection).intersection(set(chain(a, b))))
#         else:
#             object_list_intersection = self.model.objects.order_by(sort_type)
#         return object_list_intersection


class PostUpdateView(OwnerRequiredMixin, UpdateWithInlinesView):
    model = Post
    inlines = [ImagesInline]
    form_class = PostUpdateForm
    template_name = 'board/post_update_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['image_helper'] = ImageHelper()
        return context

    def get_success_url(self):
        messages.success(self.request, 'Post updated!', extra_tags='fa fa-check')
        return self.object.get_absolute_url()
