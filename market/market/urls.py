"""market URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
"""
from django.conf.urls import url, include
from django.contrib import admin

from django.views.generic.base import TemplateView
import market.apps.board.views as views
from market.apps.board.backends import MyRegistrationView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^test/', TemplateView.as_view(template_name='example.html')),
    url(r'^accounts/register/$', MyRegistrationView.as_view(), name='registration_register'),
    url(r'^accounts/create_post/$', views.create_post, name='registration_create_post'),
    url(r'posts/(?P<slug>[-\w]+)/edit/$', views.edit_post, name='edit_post'),
    url(r'posts/(?P<slug>[-\w]+)/$', views.post_detail, name='post_detail'),

    url(r'^accounts/', include('registration.backends.simple.urls')),
    # END OF REGISTRATION URLS
]
