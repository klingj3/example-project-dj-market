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
    url(r'^', include('market.apps.board.urls')),
    url(r'^test/', TemplateView.as_view(template_name='example.html')),

    url(r'^accounts/register/', MarketRegistrationView.as_view(), name='registration_register'),
    url(r'^accounts/', include('registration.backends.simple.urls')),

    # Board app
    url(r'^posts/', include('market.apps.board.urls')),
]
