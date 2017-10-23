from django.conf import settings
from django.db import models
from django.urls import reverse

from autoslug import AutoSlugField


class SocialProfile(RandomSlugModel):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    avatar = models.ImageField(null=True)
    name = models.CharField(max_length=200)
    organization_name = models.CharField(max_length=300, blank=True)
    bio = models.TextField(blank=True)

    # Location to be changed here, same as in posts.
    location = models.CharField(max_length=5)
    public_email = models.EmailField(max_length=300, blank=True)
    public_website = models.URLField(max_length=300, blank=True)
    social_url = models.CharField(max_length=300, unique=True)

    def get_absolute_url(self):
        return reverse('social:detail', kwargs={'slug': self.social_url})
