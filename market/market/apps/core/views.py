from django.urls import reverse

from registration.backends.simple.views import RegistrationView

class MarketRegistrationView(RegistrationView):
    template_name = 'registration/registration_form.html'

    def get_success_url(self, user):
        return reverse('board:list')

