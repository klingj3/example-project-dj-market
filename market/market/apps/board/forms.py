from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import (Div,
                                 Field,
                                 Fieldset,
                                 Layout,
                                 MultiField,
                                 Submit)

from market.apps.board.models import Post
from market.apps.core.mixins import CreateWithOwnerMixin


class PostForm(CreateWithOwnerMixin, forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            Fieldset(
                'test',
                Field('title', placeholder='A snappy title'),
                'body',
                'tags',
                'price',
                'unit',
                'location'
            ),
        )


class PostUpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body', 'tags', 'activate_date', 'deactivate_date', 'price', 'unit', 'location']

