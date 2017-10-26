"""market URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
"""
from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    # Remove logout confirmation
    # Note: Needs to be changed to redirect to ACCOUNT_LOGOUT_REDIRECT_URL
    # url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
    url(r'^accounts/', include('allauth.urls')),

    # Social app
    url(r'^', include('market.apps.social.urls')),

    # Board app
    url(r'^', include('market.apps.board.urls')),
]
