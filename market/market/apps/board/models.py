from django.contrib.auth.models import User
from django.db import models

from autoslug import AutoSlugField
from django_measurement.models import MeasurementField
from django_prices.models import PriceField


class Post(models.Model):
    UNIT_CHOICES = (
        ('pound', 'POUND'),
        ('gallon', 'GALLON'),
        ('each', 'EACH'),
    )

    user = models.ForeignKey(User, editable=False)
    slug = AutoSlugField(unique=True)
    post_date = models.DateTimeField(auto_now_add=True)

    title = models.CharField(max_length=300)
    body = models.TextField(max_length=5000)

    # price = PriceField(currency='USD', max_digits=5, decimal_places=2)
    price = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    # unit = MeasurementField()
    unit = models.CharField(max_length=80, choices=UNIT_CHOICES, default='each')

    location = models.CharField(max_length=5)
