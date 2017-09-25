from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField(max_length=1023)
    #price = PriceField('Price', currency='USD', max_digits = 5, decimal_places=2)
    UNIT_CHOICES = [('Lb', 'LB'),
                    ('Gallon', 'GALLON'),
                    ('each', 'EACH'),
                    ]
    unit = models.CharField(max_length=7, choices=UNIT_CHOICES, default='each')
    location = models.CharField(max_length=5)
    postDate = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True)