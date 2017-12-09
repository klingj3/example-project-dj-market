from django.contrib import messages
from django.urls import reverse
from django.db.models import Q
from django.views.generic import (DeleteView,
                                  DetailView,
                                  ListView,
                                  TemplateView)

from extra_views import (CreateWithInlinesView,
                         InlineFormSet,
                         UpdateWithInlinesView)
from functools import reduce
from itertools import chain
from operator import and_, or_
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
        context['similar_posts'] = self.model.objects.search(tags=self.object.tags.get_tag_list()).exclude(id=self.object.id)[:4]
        return context

# View for displaying searches
class PostSearchView(ListView):
    model = Post
    template_name = 'board/post_list.html'
    # No pagination for now, breaks searches
    # paginate_by = 8

    # Get the more specific results
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get('q', '')
        if query != '':
            sort_rule = self.request.GET.get('sort')
            sort_type = 'modified'
            if sort_rule:
                if sort_rule == 'date-newest':
                    sort_type = ('modified')
                elif sort_rule == 'date-oldest':
                    sort_type = ('-modified')
                elif sort_rule == 'price-lowest':
                    sort_type = ('price')
                elif sort_rule == 'price-highest':
                    sort_type = ('-price')
            search_terms = query.split()
            list = self.model.objects.filter(reduce(or_, [Q(title__icontains=term) | Q(tags__name=term) \
                                                         for term in search_terms])).order_by(sort_type, 'title')
            # If we were using postgres, this could be done by adding distinct to the end of the preceeding line.
            # In the meantime, here's a slightly longer solution.
            seen = []
            seen_add = seen.append
            list = [obj for obj in list if not (obj in seen or seen_add(obj))]
            context['post_list'] = list
        else:
            context['post_list'] = []
        return context

    # Get the more general results.
    def get_queryset(self):
        # TODO: Pre-process search query for better usability

        query = self.request.GET.get('q', '')

        # Sort by specified rule, then title
        sort_rule = self.request.GET.get('sort')
        sort_type = 'modified'
        if sort_rule:
            if sort_rule == 'date-newest':
                sort_type = ('modified')
            elif sort_rule == 'date-oldest':
                sort_type = ('-modified')
            elif sort_rule == 'price-lowest':
                sort_type = ('price')
            elif sort_rule == 'price-highest':
                sort_type = ('-price')

        if query != '':
            search_terms = query.split()
            qs = self.model.objects.order_by(sort_type, 'title')
            for term in search_terms:
                qs = qs.filter(Q(title__icontains=term) | Q(tags__name__icontains=term))
            # If we were using postgres, this could be done by adding distinct to the end of the preceeding line.
            # In the meantime, here's a slightly longer solution.
            seen = []
            seen_add = seen.append
            qs = [obj for obj in qs if not (obj in seen or seen_add(obj))]
        else:
            qs = self.model.objects.order_by(sort_type, 'title')
        return qs


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
