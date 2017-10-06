from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import HttpResponseForbidden
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from django.views.generic import (DetailView,
                                  FormView,
                                  ListView,
                                  RedirectView,
                                  UpdateView)

from market.apps.core.mixins import UserIsOwnerMixin
from market.apps.social.forms import (UserProfileForm,
                                      UserProfileEditForm)
from market.apps.social.models import UserProfile


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
        messages.success(self.request, 'Account detail successfully updated!', extra_tags='fa fa-check')
        return reverse('board:list')


class UserProfileUpdateView(UserIsOwnerMixin, UpdateView):
    model = UserProfile
    form_class = UserProfileEditForm
    template_name = 'social/profile_form.html'

    def get_success_url(self):
        messages.success(self.request, 'Account detail successfully updated!', extra_tags='fa fa-check')
        return reverse('board:list')
