from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import (DetailView,
                                  FormView,
                                  ListView,
                                  RedirectView,
                                  UpdateView)

from market.apps.board.models import Post
from market.apps.core.mixins import (CreateWithOwnerMixin,
                                     OwnerRequiredMixin,
                                     SellerRequiredMixin)
from market.apps.social.forms import SocialProfileUpdateForm
from market.apps.social.models import SocialProfile


class SocialProfileSelfDetailView(SellerRequiredMixin, DetailView):
    model = SocialProfile
    template_name = 'social/profile_detail.html'

    def get_object(self, *args, **kwargs):
        return SocialProfile.objects.get(owner=self.request.profile)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts_list'] = Post.objects.filter(owner=self.request.profile)
        return context


class SocialProfileDetailView(DetailView):
    model = SocialProfile
    context_object_name = 'profile'
    template_name = 'social/profile_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts_list'] = Post.objects.filter(owner=self.object.owner)
        return context


# class SocialProfileListView(ListView):
#     model = SocialProfile
#     template_name = 'social/browse.html'
#     paginate_by = 8


class SocialProfileUpdateView(SellerRequiredMixin, OwnerRequiredMixin, UpdateView):
    model = SocialProfile
    form_class = SocialProfileUpdateForm
    template_name = 'social/profile_update_form.html'

    def get_object(self, *args, **kwargs):
        return SocialProfile.objects.get(owner=self.request.profile)

    def get_success_url(self):
        messages.success(self.request, 'Seller profile updated!', extra_tags='fa fa-check')
        return reverse('social:update')
