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
        context['similar_posts'] = self.model.objects.search(tags=self.object.tags.get_tag_list()).exclude(id=self.object.id)[:4]
        return context


class PostSearchView(ListView):
    model = Post
    template_name = 'board/post_list.html'

    # No pagination for now, breaks searches
    # paginate_by = 8

    def get_queryset(self):
        # TODO: Pre-process search query for better usability

        query = self.request.GET.get('q', '')
        qs = self.model.objects.search(query=query)

        # Sort by specified rule, then title
        sort_rule = self.request.GET.get('sort')
        if sort_rule:
            if sort_rule == 'date-newest':
                qs = qs.order_by('modified', 'title')
            elif sort_rule == 'date-oldest':
                qs = qs.order_by('-modified', 'title')
            elif sort_rule == 'price-lowest':
                qs = qs.order_by('price', 'title')
            elif sort_rule == 'price-highest':
                qs = qs.order_by('-price', 'title')

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
