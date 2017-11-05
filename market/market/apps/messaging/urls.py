from django.conf.urls import url

from market.apps.messaging.views import (MessageCreateView,
                                        MessageDetailView,
                                        MessageListView,
                                        )


app_name = 'messaging'
urlpatterns = [
    url(r'^$', MessageListView.as_view(), name='inbox'),
    url(r'^new/$', MessageCreateView.as_view(), name='send'),
    url(r'^(?P<slug>[-\w]+)/$', MessageDetailView.as_view(), name='detail'),
]
