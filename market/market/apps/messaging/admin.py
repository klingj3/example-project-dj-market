# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from market.apps.messaging.models import Message


class MessageAdmin(admin.ModelAdmin):
    model = Message
    list_display = ('sender', 'recipient', 'subject')


admin.site.register(Message, MessageAdmin)
