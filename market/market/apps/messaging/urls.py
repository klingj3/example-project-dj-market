from django.conf.urls import url

from market.apps.messaging.views import (MessageCreateView,
                                        MessageDetailView,
                                        MessageListView,
                                        ReviewCreateView,
                                        ReviewDetailView,
                                        ReviewListView,
                                        )


app_name = 'messaging'
urlpatterns = [
    url(r'messaging/^$', MessageListView.as_view(), name='inbox'),
    url(r'^messaging/new/(?P<slug>[-\w]+)', MessageCreateView.as_view(), name='new_message'),
    url(r'^messaging/(?P<slug>[-\w]+)/$', MessageDetailView.as_view(), name='detail_message'),
    url(r'^reviews/new/(?P<slug>[-\w]+)/$', ReviewCreateView.as_view(), name='new_review'),
    url(r'^reviews/(?P<slug>[-\w]+)/$', ReviewDetailView.as_view(), name='detail_review'),
    url(r'reviews/user/(?P<slug>[-\w]+)/^$', MessageListView.as_view(), name='reviews_for_user'),
]
