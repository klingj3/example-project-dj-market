from django.db import models
from django.conf import settings

from django_extensions.db.fields import RandomCharField

# Used to generate the random URLs for profiles, posts, and other.
class RandomSlugModel(models.Model):
    slug = RandomCharField(length=8, lowercase=True, unique=True)

    class Meta:
        abstract = True


class UserProfile(RandomSlugModel):
    """
    This is an extension to the default User model, created on
    registration for each user. All relations to a User are through
    this model to maintain separation from the authentication backend.
    """
    ACCOUNT_TYPE_CHOICES = (
        ('0', "I'm a buyer"),
        ('1', "I'm a seller"),
    )

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')

    type = models.CharField(max_length=1, choices=ACCOUNT_TYPE_CHOICES, default='0')
    name = models.CharField('name', max_length=200)
    @property
    def is_seller(self):
        return self.type == self.ACCOUNT_TYPE_CHOICES[1][0]

    def __str__(self):
        return self.name
