from django.conf.urls import url

from market.apps.social.views import (
                                    ProfileDetailView,
                                    UserProfileCreateView,
                                    UserProfileUpdateView,
                                    ProfileBrowseView,
                                    )


app_name = 'social'
urlpatterns = [
    url(r'^new/$', UserProfileCreateView.as_view(), name='new'),
    url(r'^browse/$', ProfileBrowseView.as_view(), name='browse'),
    url(r'^(?P<slug>[-\w]+)/edit/$', UserProfileUpdateView.as_view(), name='update'),
    url(r'^(?P<slug>\w+)/$', ProfileDetailView.as_view(), name='detail'),
]
