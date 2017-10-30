from django import forms

from crispy_forms.bootstrap import FormActions
from crispy_forms.helper import FormHelper
from crispy_forms.layout import (Field,
                                 Fieldset,
                                 HTML,
                                 Layout,
                                 Submit)

from market.apps.board.models import Post


class ImageHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.layout = Layout(
        #     'image'
        # )
        # TODO: Template for image view
        self.template = 'bootstrap/table_inline_formset.html'
        self.form_tag = False
        self.disable_csrf = True


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body', 'tags', 'price', 'unit', 'location']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            Fieldset(
                '',
                Field('title', placeholder='A snappy title'),
                'body',
                'tags',
                'price',
                'unit',
                'location'
            ),
            FormActions(
                Submit('submit', 'Create Post', css_class='btn btn-success'),
            )
        )
        self.helper.form_tag = False


class PostUpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body', 'tags', 'price', 'unit', 'location']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            Fieldset(
                '',
                Field('title', placeholder='A snappy title'),
                'body',
                'tags',
                'price',
                'unit',
                'location'
            ),
            FormActions(
                Submit('submit', 'Update Post', css_class='btn btn-success'),
            )
        )
        self.helper.form_tag = False
