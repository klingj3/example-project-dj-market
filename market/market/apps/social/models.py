# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=31, default = '')
    last_name = models.CharField(max_length=31, default = '')
    organization_name = models.CharField(max_length=127, default = '')
    bio = models.CharField(max_length=1023, blank=True)
    # Location to be changed here, same as in posts.
    location = models.CharField(max_length=5, default='12180')
    public_email = models.CharField(max_length=48)