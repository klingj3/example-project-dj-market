from django.contrib import messages
from django.urls import reverse
from django.views.generic import (DetailView,
                                  FormView,
                                  ListView,
                                  UpdateView)

from market.apps.core.mixins import (CreateWithOwnerMixin,
                                     OwnerRequiredMixin)
from market.apps.social.forms import (UserProfileEditForm,
                                      UserProfileForm)
from market.apps.social.models import UserProfile


class UserProfileListView(ListView):
    model = UserProfile
    template_name = 'social/browse.html'
    paginate_by = 8


class UserProfileDetailView(DetailView):
    model = UserProfile
    template_name = 'social/profile_detail.html'


# TODO: Profile automatically created based on seller status
class UserProfileCreateView(CreateWithOwnerMixin, FormView):
    form_class = UserProfileForm
    template_name = 'social/profile_form.html'

    def get_success_url(self):
        messages.success(self.request, 'Account detail successfully updated!', extra_tags='fa fa-check')
        return reverse('board:list')


class UserProfileUpdateView(OwnerRequiredMixin, UpdateView):
    model = UserProfile
    form_class = UserProfileEditForm
    template_name = 'social/profile_form.html'

    def get_success_url(self):
        messages.success(self.request, 'Account detail successfully updated!', extra_tags='fa fa-check')
        return reverse('board:list')
