# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.shortcuts import render
from market.apps.social.models import UserProfile
from market.apps.social.forms import UserProfileForm

from django.views.generic import (CreateView,)

class UserProfileCreateView(CreateView):
    model = UserProfile
    form_class = UserProfileForm
    template_name = 'social/profile_form.html'
    def get_success_url(self):
        messages.success(self.request, 'Account detail successfully updated!', extra_tags='fa fa-check')
        return reverse('board:list')