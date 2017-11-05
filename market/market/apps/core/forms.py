from django import forms

from allauth.account.forms import (SignupForm,
                                   LoginForm)
# from crispy_forms.bootstrap import FormActions
from crispy_forms import bootstrap
from crispy_forms.helper import FormHelper
from crispy_forms import layout
# from crispy_forms.layout import (Div,
#                                  Field,
#                                  Fieldset,
#                                  Layout,
#                                  MultiField,
#                                  Submit)

from market.apps.core.models import UserProfile


class MarketLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper(self)
        self.helper.layout = layout.Layout(
            layout.Fieldset(
                '',
                'login',
                layout.Field('password', help_text='blarg')
            ),
            bootstrap.FormActions(
                layout.Submit('submit', 'Log in', css_class='btn btn-success'),
            ),
        )


class MarketSignupForm(SignupForm):
    type = forms.ChoiceField(choices=UserProfile.ACCOUNT_TYPE_CHOICES)
    name = forms.CharField(max_length=200)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # TODO: Add help texts
        self.helper = FormHelper(self)
        self.helper.layout = layout.Layout(
            layout.Fieldset(
                '',
                'email',
                'type',
                'name',
                'password1',
                'password2',
            ),
            bootstrap.FormActions(
                layout.Submit('submit', 'Create an account', css_class='btn btn-success'),
            ),
        )
