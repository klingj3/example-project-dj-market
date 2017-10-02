from django.contrib import messages
from django.urls import reverse

from registration.backends.simple.views import RegistrationView


class MarketRegistrationView(RegistrationView):
    template_name = 'core/registration_form.html'

    def get_success_url(self):
        messages.success(self.request, 'Account created!', extra_tags='fa fa-check')
        return reverse('board:list')
