from django.contrib import admin

from market.apps.social.models import (Review,
                                       SocialProfile)


admin.site.register(Review)
admin.site.register(SocialProfile)
