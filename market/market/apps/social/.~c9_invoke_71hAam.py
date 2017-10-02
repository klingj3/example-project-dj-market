# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from autoslug import AutoSlugField
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=63, default = '')
    organization_name = models.CharField(max_length=127)
    bio = models.TextField(blank=True)
    # Location to be changed here, same as in posts.
    location = models.CharField(max_length=5)
    public_email = models.EmailField(max_length=31, blank=True)
    public_website = models.CharField(max_length=31, blank=True)
    slug = AutoSlugField(unique=True)

    def __unicode__(self):
        return u"%s" % self.user