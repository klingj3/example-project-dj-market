from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import (DetailView,
                                  FormView,
                                  ListView,
                                  RedirectView,
                                  UpdateView)

from market.apps.board.models import Post
from market.apps.core.mixins import (CreateWithOwnerMixin,
                                     OwnerRequiredMixin)
# from market.apps.social.forms import SocialProfileEditForm
from market.apps.social.models import SocialProfile

class SelfRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False
    query_string = True

    def get_redirect_url(self):
        profile = UserProfile.objects.get(owner=self.request.user)
        if profile:
            return reverse('social:detail', kwargs={'slug': profile.social_url})
        else:
            return reverse('social:create')

class SocialProfileListView(ListView):
    model = SocialProfile
    template_name = 'social/browse.html'
    paginate_by = 8


class SocialProfileDetailView(DetailView):
    model = SocialProfile
    template_name = 'social/profile_detail.html'
    def get_context_data(self, **kwargs):
        context = super(UserProfileDetailView, self).get_context_data(**kwargs)
        context['Posts'] = Post.objects.filter(owner=self.request.user)
        return context


# class SocialProfileUpdateView(OwnerRequiredMixin, UpdateView):
#     model = SocialProfile
#     form_class = SocialProfileEditForm
#     template_name = 'social/profile_form.html'
#
#     def get_success_url(self):
#         messages.success(self.request, 'Account detail successfully updated!', extra_tags='fa fa-check')
#         # TODO: Reverse to own detail view
#         return reverse('board:list')
