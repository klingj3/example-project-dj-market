from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        UserPassesTestMixin)
from django.db import models
from django.urls import reverse


class CreateWithOwnerMixin(LoginRequiredMixin):
    """
    Injects the currently logged in user to the 'owner' field
     of the form in this view.
    """
    def get_form(self, form_class=None):
        form = super(CreateWithOwnerMixin, self).get_form(form_class)
        # We know request has a user due to LoginRequiredMixin
        form.instance.owner = self.request.user

        return form


class OwnerRequiredMixin(UserPassesTestMixin):
    """
    Blocks access if the currently logged in user is not the
     owner of the object in this single object view.
    """
    raise_exception = True

    def test_func(self):
        # Assumes this has a get_object attribute
        # Could test with hasattr()?
        return self.request.user == self.get_object().owner
