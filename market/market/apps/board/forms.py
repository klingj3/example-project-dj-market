from django.forms import ModelForm

from market.apps.board.models import Post

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'body', 'unit', 'location',)