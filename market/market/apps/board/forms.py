from django import forms

from market.apps.board.models import Post
from market.apps.core.mixins import CreateWithOwnerMixin


class PostForm(CreateWithOwnerMixin, forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body', 'tags', 'activate_date', 'deactivate_date', 'price', 'unit', 'location']


class PostUpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body', 'tags', 'activate_date', 'deactivate_date', 'price', 'unit', 'location']

