from django import forms

from crispy_forms import (bootstrap,
                          layout)
from crispy_forms.helper import FormHelper

from leaflet.forms.widgets import LeafletWidget

from market.apps.board.models import Post

# Form to handle the niput of images.
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

# Post Input
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body', 'tags', 'price', 'unit', 'location']
        widgets = {'location': LeafletWidget()}

    # Appearance of the Form
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper(self)
        self.helper.layout = layout.Layout(
            layout.Fieldset(
                '',
                layout.Field('title', placeholder='A snappy title'),
                'body',
                'tags',
                bootstrap.PrependedAppendedText('price', '$', 'USD'),
                'unit',
                'location'
            ),
            bootstrap.FormActions(
                layout.Submit('submit', 'Create post', css_class='btn btn-success'),
            )
        )
        self.helper.form_tag = False


class PostUpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body', 'tags', 'price', 'unit', 'location']
        widgets = {'location': LeafletWidget()}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # TODO: Don't repeat from the PostForm
        self.helper = FormHelper(self)
        self.helper.layout = layout.Layout(
            layout.Fieldset(
                '',
                layout.Field('title', placeholder='A snappy title'),
                'body',
                'tags',
                bootstrap.PrependedText('price', '$'),
                'unit',
                'location'
            ),
            bootstrap.FormActions(
                layout.Submit('submit', 'Update post', css_class='btn btn-success'),
                layout.HTML('<a class="btn btn-outline-secondary" href="{% url "board:detail" slug=object.slug %}">Cancel</a>'),
            )
        )
        self.helper.form_tag = False
