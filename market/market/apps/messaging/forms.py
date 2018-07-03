from django import forms

from crispy_forms import bootstrap
from crispy_forms import layout
from crispy_forms.helper import FormHelper
from crispy_forms.layout import (Field,
                                 Fieldset,
                                 HTML,
                                 Layout,
                                 Submit)

from market.apps.messaging.models import Message

# Form through which messages can be sent.
class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['recipient', 'subject', 'body', 'referenced_post']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            layout.Fieldset(
                '',
                layout.Field('recipient', readonly=True),
                'subject',
                'body',
                'referenced_post',
            ),
            bootstrap.FormActions(
                Submit('submit', 'Send Message', css_class='btn btn-success'),
            )
        )
        self.helper.form_tag = False