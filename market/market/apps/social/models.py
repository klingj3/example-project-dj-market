from django.db import models
from django_extensions.db.models import (ActivatorModel,
                                         TimeStampedModel)
from django.urls import reverse

from djgeojson.fields import PointField

from market.apps.core.models import (RandomSlugModel,
                                     UserProfile)


# Model for user-to-user reviews.
class Review(RandomSlugModel, TimeStampedModel):
    reviewer = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='reviewer')
    reviewee = models.ForeignKey(UserProfile, default=1, on_delete=models.CASCADE, related_name='reviewee')
    title = models.CharField(max_length=128)
    SCORE_CHOICES = [
                    (1, '1'),
                    (2, '2'),
                    (3, '3'),
                    (4, '4'),
                    (5, '5'),
        ]
    score = models.IntegerField(choices=SCORE_CHOICES, default=4)
    body = models.TextField(max_length=5000)
    def get_absolute_url(self):
        return reverse('messaging:review_deteail', kwargs={'slug': self.slug})


# The SocialProfile is a model used by Sellers through which they detail themselves
# and/or provide additional information on their services.
class SocialProfile(RandomSlugModel):
    owner = models.OneToOneField(UserProfile, on_delete=models.CASCADE, related_name='social')

    avatar = models.ImageField(null=True, blank=True)
    tagline = models.CharField(max_length=150, blank=True)
    bio = models.TextField(max_length=2000, blank=True)

    # Location to be changed here, same as in posts.
    location = PointField()

    def get_absolute_url(self):
        return reverse('social:detail', kwargs={'slug': self.slug})
