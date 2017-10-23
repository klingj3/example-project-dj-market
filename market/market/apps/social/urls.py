from django.conf.urls import url

from market.apps.social.views import (SocialProfileDetailView,
                                      SocialProfileListView,)
                                      # SocialProfileUpdateView)


app_name = 'social'
urlpatterns = [
    url(r'^$', SocialProfileListView.as_view(), name='list'),
    # url(r'^new/$', UserProfileCreateView.as_view(), name='create'),
    # url(r'^(?P<slug>[-\w]+)/edit/$', SocialProfileUpdateView.as_view(), name='update'),
    url(r'^(?P<slug>\w+)/$', SocialProfileDetailView.as_view(), name='detail'),
]
