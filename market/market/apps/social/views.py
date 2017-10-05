# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseForbidden
from django.urls import reverse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from market.apps.social.models import UserProfile
from market.apps.social.forms import (UserProfileForm,
                                      UserProfileEditForm)
from django.shortcuts import get_object_or_404
from django.views.generic import (
                                  DetailView,
                                  FormView,
                                  ListView,
                                  RedirectView,
                                  UpdateView,
                                )


class ProfileBrowseView(ListView):
    model = UserProfile
    template_name = 'social/browse.html'
    paginate_by = 8

class ProfileDetailView(DetailView):
    model = UserProfile
    template_name = 'social/profile_detail.html'

class UserProfileCreateView(FormView):
    form_class = UserProfileForm
    template_name = 'social/profile_form.html'

    def form_valid(self, form):
        form.save(self.request.user)
        return super(UserProfileCreateView, self).form_valid(form)

    def get_success_url(self):
        messages.success(self.request, 'Account detail successfully updated!', extra_tags='fa fa-check')
        return reverse('board:list')

class UserProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = UserProfile
    form_class = UserProfileEditForm
    template_name = 'social/profile_form.html'

    def dispatch(self, request, *args, **kwargs):
        """ Make sure that only the owner can edit this page. """
        obj = self.get_object()
        if obj.user != self.request.user:
            return HttpResponseForbidden()
        return super(UserProfileUpdateView, self).dispatch(request, *args, **kwargs)
        
    def get_success_url(self, *args, **kwargs):
        messages.success(self.request, 'Account detail successfully updated!', extra_tags='fa fa-check')
        return reverse('board:list')