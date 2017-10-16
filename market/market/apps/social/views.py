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

from market.apps.core.mixins import (CreateWithOwnerMixin,
                                     OwnerRequiredMixin)
from market.apps.social.forms import (UserProfileEditForm,
                                      UserProfileForm)
from market.apps.social.models import UserProfile

class SelfRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False
    query_string = True

    def get_redirect_url(self):
        profile = UserProfile.objects.get(owner=self.request.user)
        if profile:
            return reverse('social:detail', kwargs={'slug': profile.social_url})
        else:
            return reverse('social:create')

class UserProfileListView(ListView):
    model = UserProfile
    template_name = 'social/browse.html'
    paginate_by = 8


class UserProfileDetailView(DetailView):
    model = UserProfile
    template_name = 'social/profile_detail.html'


# TODO: Profile automatically created based on seller status
class UserProfileCreateView(FormView):
    form_class = UserProfileForm
    template_name = 'social/profile_form.html'

    def form_valid(self, form):
        form.save(self.request.user)
        return super(UserProfileCreateView, self).form_valid(form)

    def get_success_url(self):
        messages.success(self.request, 'Profile successfully created!', extra_tags='fa fa-check')
        return reverse('social:me')


class UserProfileUpdateView(OwnerRequiredMixin, UpdateView):
    model = UserProfile
    form_class = UserProfileEditForm
    template_name = 'social/profile_form.html'

    def get_success_url(self):
        messages.success(self.request, 'Profile successfully updated!', extra_tags='fa fa-check')
        return reverse('social:me')
