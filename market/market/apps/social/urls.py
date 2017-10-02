from django.conf.urls import url

from market.apps.social.views import (
                                    ProfileDetailView,
                                    UserProfileCreateView,
                                    )


app_name = 'social'
urlpatterns = [
    url(r'^new/$', UserProfileCreateView.as_view(), name='create'),
    url(r'profile/(?P<username>\w+)/$', ProfileDetailView.as_view(), name='detail')
]
