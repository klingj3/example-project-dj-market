from django.forms import ModelForm

from market.apps.board.models import Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body', 'price', 'unit', 'location',]

    def form_valid(self, form):
        # Set with current user. TODO: Create a mixin for this
        self.object = form.save(commit=False)
        if self.request.user.is_authenticated():
            self.object.user = self.request.user
        self.object.save()
        
        return super(PostForm, self).form_valid(form)
