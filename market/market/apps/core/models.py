from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import (AbstractBaseUser,
                                        PermissionsMixin)

from django_extensions.db.fields import RandomCharField


class RandomSlugModel(models.Model):
    slug = RandomCharField(length=8, lowercase=True, unique=True)

    class Meta:
        abstract = True


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('TODO: Email message here')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    ACCOUNT_TYPE_CHOICES = (
        ('0', 'buyer'),
        ('1', 'seller'),
    )

    email = models.EmailField('email address', unique=True)
    name = models.CharField('name', max_length=200)
    type = models.CharField(max_length=1, choices=ACCOUNT_TYPE_CHOICES)
    date_joined = models.DateTimeField('date joined', auto_now_add=True)
    is_active = models.BooleanField('active', default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'type']

    objects = UserManager()

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name
