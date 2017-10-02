"""market URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic.base import TemplateView

from market.apps.core.views import MarketRegistrationView


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^test/', TemplateView.as_view(template_name='example.html')),

    # Account management
    url(r'^accounts/', include('registration.backends.simple.urls')),

    # Social management, could be merged under the accounts label later.
    url(r'^social/', include('market.apps.social.urls')),

    # Board app
    url(r'^', include('market.apps.board.urls')),
]
