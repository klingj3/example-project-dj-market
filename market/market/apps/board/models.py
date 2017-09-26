from django.contrib.auth.models import User
from django.db import models

from autoslug import AutoSlugField


class Post(models.Model):
    user = models.ForeignKey(User, editable=False)
    slug = AutoSlugField(unique=True)
    post_date = models.DateTimeField(auto_now_add=True)

    title = models.CharField(max_length=300)
    body = models.TextField(max_length=5000)

    price = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    unit = models.CharField(max_length=7, choices=UNIT_CHOICES, default='each')

    location = models.CharField(max_length=5)
