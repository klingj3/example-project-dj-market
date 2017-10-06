from __future__ import unicode_literals

from django.contrib import admin

from market.apps.social.models import UserProfile

# Register your models here.
admin.site.register(UserProfile)
