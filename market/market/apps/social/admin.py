from django.contrib import admin

from market.apps.social.models import (Review,
                                       SocialProfile)


# Make the reviews and social profiles visible through Django Admin
admin.site.register(Review)
admin.site.register(SocialProfile)
