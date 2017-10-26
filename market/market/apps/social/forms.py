from django import forms

from crispy_forms.bootstrap import FormActions
from crispy_forms.helper import FormHelper
from crispy_forms.layout import (Field,
                                 Fieldset,
                                 HTML,
                                 Layout,
                                 Submit)

from market.apps.core.models import UserProfile
from market.apps.social.models import SocialProfile


class UserProfileForm(forms.Form):
    # This form is used in registration to automatically create both UserProfile and SocialProfile objects
    # Note that this is NOT the form actually seen by the user

    def signup(self, request, user):
        # Automatically create user profile for every user
        profile = UserProfile.objects.create(user=user, type=self.cleaned_data['type'], name=self.cleaned_data['name'])

        # Create an empty SocialProfile if the user is a seller
        if profile.is_seller():
            SocialProfile.objects.create(owner=profile)


class SocialProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = SocialProfile
        fields = ['avatar', 'tagline', 'bio', 'location']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            Fieldset(
                '',
                'avatar',
                'tagline',
                'bio',
                'location'
            ),
            FormActions(
                Submit('submit', 'Update Profile', css_class='btn btn-success'),
            )
        )
