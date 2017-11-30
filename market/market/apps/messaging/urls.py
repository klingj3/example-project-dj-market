from django.conf.urls import url

from market.apps.messaging.views import (MessageCreateView,
                                        MessageDetailView,
                                        MessageListView,
                                        )


app_name = 'messaging'
urlpatterns = [
    url(r'^$', MessageListView.as_view(), name='inbox'),
    url(r'^new/(?P<slug>[-\w]+)', MessageCreateView.as_view(), name='new'),
    url(r'^(?P<slug>[-\w]+)/$', MessageDetailView.as_view(), name='detail'),
]
