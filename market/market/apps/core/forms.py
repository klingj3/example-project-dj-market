from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import (Div,
                                 Field,
                                 Fieldset,
                                 Layout,
                                 MultiField,
                                 Submit)
from registration.forms import RegistrationForm

from market.apps.core.models import User


class UserRegistrationForm(RegistrationForm):
    class Meta:
        model = User
        fields = '__all__'
        # fields = [UsernameField(), 'email', 'name', 'type']

    # def __init__(self, *args, **kwargs):
    #     super(PostForm, self).__init__(*args, **kwargs)
    #
    #     self.helper = FormHelper(self)
    #     self.helper.layout = Layout(
    #         Fieldset(
    #             'test',
    #             Field('title', placeholder='A snappy title'),
    #             'body',
    #             'tags',
    #             'price',
    #             'unit',
    #             'location'
    #         ),
    #     )
