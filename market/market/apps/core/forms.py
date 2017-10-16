from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import (Div,
                                 Field,
                                 Fieldset,
                                 Layout,
                                 MultiField,
                                 Submit)

from market.apps.core.models import User


# TODO: Extend allauth forms, make crispy
# This one also contains extra field
class SignupForm(forms.Form):
    type = forms.CharField()
