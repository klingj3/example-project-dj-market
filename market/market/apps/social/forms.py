from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from market.apps.social.models import UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('name', 'organization_name', 'bio', 'location', 'public_email', 'public_website', 'social_url')
        labels ={
            'name':_("Your Name"),
            'organization_name':_("Your Organization's Name"),
            'bio':_("Bio - What should your buyers know?"),
            'public_email':_("Public Email"),
            'public_website':_("Website"),
            'social_url':_("Customize your url! [websiteurl]/sellers/..."),
        }

    def save(self, user=None):
        user_profile = super(UserProfileForm, self).save(commit=False)
        if user:
            user_profile.user = user
        user_profile.save()
        return user_profile