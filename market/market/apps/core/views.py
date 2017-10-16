from django.contrib import messages
from django.urls import reverse

from registration.backends.simple.views import RegistrationView

from market.apps.core.forms import UserRegistrationForm


class MarketRegistrationView(RegistrationView):
    form_class = UserRegistrationForm

    def get_success_url(self, user):
        messages.success(self.request, 'Account created!', extra_tags='fa fa-check')
        return reverse('social:create')
