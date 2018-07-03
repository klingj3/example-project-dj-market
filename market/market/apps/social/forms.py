from django import forms

from crispy_forms import (bootstrap,
                          layout)
from crispy_forms.helper import FormHelper
from leaflet.forms.widgets import LeafletWidget

from market.apps.core.models import UserProfile
from market.apps.social.models import (Review,
                                       SocialProfile)


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['reviewee', 'score', 'title', 'body']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout = layout.Layout(
            layout.Fieldset(
                '',
                layout.Field('reviewee', readonly=True),
                'score',
                'title',
                'body',
            ),
            bootstrap.FormActions(
                layout.Submit('submit', 'Post Review', css_class='btn btn-success'),
            )
        )
        self.helper.form_tag = False


class SocialProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = SocialProfile
        fields = ['avatar', 'tagline', 'bio', 'location']
        widgets = {'location': LeafletWidget()}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper(self)
        self.helper.layout = layout.Layout(
            layout.Fieldset(
                '',
                'avatar',
                'tagline',
                'bio',
                'location'
            ),
            bootstrap.FormActions(
                layout.Submit('submit', 'Update profile', css_class='btn btn-success'),
            )
        )


class UserProfileForm(forms.Form):
    # This form is used in registration to automatically create both UserProfile and SocialProfile objects
    # Note that this is NOT the form actually seen by the user

    def signup(self, request, user):
        # Automatically create user profile for every user
        profile = UserProfile.objects.create(user=user, type=self.cleaned_data['type'], name=self.cleaned_data['name'])

        # Create an empty SocialProfile if the user is a seller
        if profile.is_seller:
            SocialProfile.objects.create(owner=profile)