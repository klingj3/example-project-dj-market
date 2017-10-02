# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from market.apps.social.models import UserProfile

class UserProfileAdmin(admin.ModelAdmin):
    model = UserProfile
    list_display = ('user', 'name',)
    prepopulated_fields = {'slug': ('user',)}

# Register your models here.
admin.site.register(UserProfile, UserProfileAdmin)
