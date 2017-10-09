from django.forms import ModelForm

from market.apps.board.models import Post
from market.apps.core.mixins import CreateWithOwnerMixin


class PostForm(CreateWithOwnerMixin, ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body', 'tags', 'activate_date', 'deactivate_date', 'price', 'unit', 'location',]
