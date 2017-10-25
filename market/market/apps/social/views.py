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
                                     OwnerRequiredMixin)
from market.apps.social.forms import SocialProfileUpdateForm
from market.apps.social.models import SocialProfile


# class SelfRedirectView(LoginRequiredMixin, RedirectView):
#     permanent = False
#     query_string = True
#
#     def get_redirect_url(self):
#         profile = UserProfile.objects.get(owner=self.request.user)
#         if profile:
#             return reverse('social:detail', kwargs={'slug': profile.social_url})
#         else:
#             return reverse('social:create')


class SocialProfileDetailView(DetailView):
    model = SocialProfile
    template_name = 'social/profile_detail.html'

    def get_object(self, *args, **kwargs):
        try:
            obj = super().get_object(*args, **kwargs)
        except AttributeError:
            # If we don't get an object (e.g., no slug given), display user's own profile
            obj = get_object_or_404(SocialProfile, owner=self.request.user.profile)

        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts_list'] = Post.objects.filter(owner=self.request.user.profile)
        return context


# class SocialProfileListView(ListView):
#     model = SocialProfile
#     template_name = 'social/browse.html'
#     paginate_by = 8


# TODO: Edit profile under /settings/profile
# View profile under .../<slug> or /profile
class SocialProfileUpdateView(OwnerRequiredMixin, UpdateView):
    model = SocialProfile
    form_class = SocialProfileUpdateForm
    template_name = 'social/profile_update_form.html'

    def get_object(self, *args, **kwargs):
        return get_object_or_404(SocialProfile, owner=self.request.user.profile)

    def get_success_url(self):
        messages.success(self.request, 'Profile updated successfully!', extra_tags='fa fa-check')
        # TODO: Reverse to own detail view
        return reverse('board:list')
