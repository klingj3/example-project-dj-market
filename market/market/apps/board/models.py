from django.db import models
from django.db.models import Q
from django.urls import reverse

from django_extensions.db.models import (ActivatorModel,
                                         TimeStampedModel)
from djgeojson.fields import PointField
from tagulous.models import TagField

from market.apps.core.models import (RandomSlugModel,
                                     UserProfile)


class PostManager(models.Manager):
    def search(self, **kwargs):
        qs = super().get_queryset()

        # TODO:
        # Split query into words, case insensitive search each field:
        # owner name, title, body, tags, location

        if 'query' in kwargs:
            query = kwargs['query']
            qs = qs.filter(Q(title__icontains=query) | Q(body__icontains=query))

        if 'tags' in kwargs:
            tags = kwargs['tags']
            # Filter to posts with tags in the provided set
            qs = qs.filter(tags__name__in=tags)

        return qs


# Posts submitted by users on the site.
class Post(RandomSlugModel, TimeStampedModel):
    UNIT_CHOICES = (
        ('pound', 'POUND'),
        ('gallon', 'GALLON'),
        ('each', 'EACH'),
    )

    # todo: custom queryset to get active posts
    objects = PostManager()

    owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    # todo: Remove activatormodel?

    title = models.CharField(max_length=300)
    body = models.TextField(max_length=5000)

    # TODO: Use autocomplete_initial=True and specify preset tags?
    tags = TagField(max_count=10, force_lowercase=True, space_delimiter=False, blank=True)

    price = models.DecimalField(max_digits=7, decimal_places=2)
    unit = models.CharField(max_length=80, choices=UNIT_CHOICES, default='each')

    # location = models.CharField(max_length=5)
    location = PointField()

    def get_absolute_url(self):
        return reverse('board:detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title + " - $" + str(self.price)


class PostImage(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(blank=True)
