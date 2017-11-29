
from django.conf import settings
from django.db import models
from django.urls import reverse

from django_extensions.db.models import (ActivatorModel,
                                         TimeStampedModel)
from geoposition.fields import GeopositionField
from tagulous.models import TagField

from market.apps.core.models import (RandomSlugModel,
                                     UserProfile)
from market.apps.board.models import Post


class Message(RandomSlugModel, TimeStampedModel):
    sender = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='sender')
    recipient = models.ForeignKey(UserProfile, default=1, on_delete=models.CASCADE, related_name='recipient')
    subject = models.CharField(max_length=128)
    referenced_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    body = models.TextField(max_length=5000)
    def get_absolute_url(self):
        return reverse('messaging:detail', kwargs={'slug': self.slug})

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
    