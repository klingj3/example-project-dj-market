from django.conf.urls import url

from market.apps.social.views import (
                                    ProfileDetailView,
                                    UserProfileCreateView,
                                    UserProfileUpdateView,
                                    )


app_name = 'social'
urlpatterns = [
    url(r'^new/$', UserProfileCreateView.as_view(), name='create'),
    url(r'^(?P<slug>[-\w]+)/edit/$', UserProfileUpdateView.as_view(), name='update'),
    url(r'profile/(?P<slug>\w+)/$', ProfileDetailView.as_view(), name='detail')
]
