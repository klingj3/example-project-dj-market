from django.forms import ModelForm
from market.apps.social.models import UserProfile
from django.contrib.auth.models import User

class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ('name', 'organization_name', 'bio', 'location', 'public_email')

    def save(self, user=None):
        user_profile = super(UserProfileForm, self).save(commit=False)
        if user:
            user_profile.user = user
        user_profile.save()
        return user_profile