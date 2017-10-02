from django.conf.urls import url

from market.apps.social.views import (UserProfileCreateView,)


app_name = 'social'
urlpatterns = [
    url(r'^new/$', UserProfileCreateView.as_view(), name='create'),
]
