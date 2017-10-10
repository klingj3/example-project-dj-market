from django.contrib import messages
from django.urls import reverse

from registration.backends.simple.views import RegistrationView


class MarketRegistrationView(RegistrationView):
    def get_success_url(self, user):
        messages.success(self.request, 'Account created!', extra_tags='fa fa-check')
        return reverse('social:create')
