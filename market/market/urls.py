"""market URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
"""
from django.conf.urls import url
from django.contrib import admin

from django.views.generic.base import TemplateView
import market.apps.board.views as views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', TemplateView.as_view(template_name='example.html')),
    url(r'^index/', views.index, name='index'),
    url(r'posts/(?P<slug>[-\w]+)/edit/$', views.edit_post, name='edit_post'),
    url(r'posts/(?P<slug>[-\w]+)/$', views.post_detail, name='post_detail'),
]
