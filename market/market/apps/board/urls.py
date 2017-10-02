from django.conf.urls import url

from market.apps.board.views import (PostCreateView,
                                     PostDeleteView,
                                     PostDetailView,
                                     PostListView,
                                     PostUpdateView)


app_name = 'board'
urlpatterns = [
    url(r'^$', PostListView.as_view(), name='list'),
    url(r'^new/$', PostCreateView.as_view(), name='create'),
    url(r'^posts/(?P<slug>[-\w]+)/edit/$', PostUpdateView.as_view(), name='update'),
    url(r'^posts/(?P<slug>[-\w]+)/delete/$', PostDeleteView.as_view(), name='delete'),
    url(r'^posts/(?P<slug>[-\w]+)/$', PostDetailView.as_view(), name='detail'),
]
