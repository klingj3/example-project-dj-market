from django.conf.urls import url

from market.apps.social.views import (ReviewCreateView,
                                      ReviewDetailView,
                                      SocialProfileDetailView,
                                      SocialProfileSelfDetailView,
                                      # SocialProfileListView,
                                      SocialProfileUpdateView)


app_name = 'social'
urlpatterns = [
    # url(r'^$', SocialProfileListView.as_view(), name='list'),
    url(r'^profile/$', SocialProfileSelfDetailView.as_view(), name='detail'),
    url(r'^profile/(?P<slug>[-\w]+)/$', SocialProfileDetailView.as_view(), name='detail'),

    # Profile is updated in settings
    url(r'^settings/profile/$', SocialProfileUpdateView.as_view(), name='update'),

    # Review urls
    url(r'^reviews/new/(?P<slug>[-\w]+)/$', ReviewCreateView.as_view(), name='new_review'),
    url(r'^reviews/(?P<slug>[-\w]+)/$', ReviewDetailView.as_view(), name='review_detail'),
]
