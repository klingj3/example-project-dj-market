from django.db import models
from django.urls import reverse

from django_extensions.db.models import TimeStampedModel

from market.apps.core.models import (RandomSlugModel,
                                     UserProfile)
from market.apps.board.models import Post


# The class for messages sent from user to user
class Message(RandomSlugModel, TimeStampedModel):
    sender = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='sender')
    recipient = models.ForeignKey(UserProfile, default=1, on_delete=models.CASCADE, related_name='recipient')
    subject = models.CharField(max_length=128)
    referenced_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    body = models.TextField(max_length=5000)

    def get_absolute_url(self):
        return reverse('messaging:detail', kwargs={'slug': self.slug})
