from django.db import models
from django.conf import settings

from django_extensions.db.fields import RandomCharField


class RandomSlugModel(models.Model):
    slug = RandomCharField(length=8, lowercase=True, unique=True)

    class Meta:
        abstract = True


class UserProfile(models.Model):
    ACCOUNT_TYPE_CHOICES = (
        ('0', "I'm a buyer"),
        ('1', "I'm a seller"),
    )

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')

    type = models.CharField(max_length=1, choices=ACCOUNT_TYPE_CHOICES, default='0')
    name = models.CharField('name', max_length=200)
