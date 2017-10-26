from django.conf import settings
from django.db import models
from django.urls import reverse

from django_extensions.db.models import (ActivatorModel,
                                         TimeStampedModel)
from geoposition.fields import GeopositionField
from tagulous.models import TagField

from market.apps.core.models import (RandomSlugModel,
                                     UserProfile)


# TODO: ActivatorModel
class Post(RandomSlugModel, TimeStampedModel):
    UNIT_CHOICES = (
        ('pound', 'POUND'),
        ('gallon', 'GALLON'),
        ('each', 'EACH'),
    )

    # todo: custom queryset to get active posts

    owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    # todo: published field
    # todo: Remove activatormodel?

    title = models.CharField(max_length=300)
    body = models.TextField(max_length=5000)

    # TODO: Use autocomplete_initial=True and specify preset tags?
    tags = TagField(max_count=10, force_lowercase=True, space_delimiter=False, blank=True)

    price = models.DecimalField(max_digits=7, decimal_places=2)
    unit = models.CharField(max_length=80, choices=UNIT_CHOICES, default='each')

    # location = models.CharField(max_length=5)
    location = GeopositionField()

    def get_absolute_url(self):
        return reverse('board:detail', kwargs={'slug': self.slug})


class PostImage(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(blank=True)
