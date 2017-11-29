from django.db import models
from django.urls import reverse

from djgeojson.fields import PointField

from market.apps.core.models import (RandomSlugModel,
                                     UserProfile)


class SocialProfile(RandomSlugModel):
    owner = models.OneToOneField(UserProfile, on_delete=models.CASCADE, related_name='social')

    avatar = models.ImageField(null=True, blank=True)
    tagline = models.CharField(max_length=150, blank=True)
    bio = models.TextField(max_length=2000, blank=True)

    # Location to be changed here, same as in posts.
    location = PointField()

    def get_absolute_url(self):
        return reverse('social:detail', kwargs={'slug': self.slug})
