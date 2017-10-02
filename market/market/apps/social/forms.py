from django.forms import ModelForm
from market.apps.social.models import UserProfile

class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ('first_name', 'last_name', 'organization_name', 'bio', 'location', 'public_email')