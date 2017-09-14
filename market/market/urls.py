"""market URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
"""
from django.conf.urls import url
from django.contrib import admin

from market.apps.board.views import TestView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', TestView.as_view()),
]
