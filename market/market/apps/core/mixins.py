from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        UserPassesTestMixin)

from market.apps.core.models import UserProfile


class CreateWithOwnerMixin(LoginRequiredMixin):
    """
    Injects the currently logged in user to the 'owner' field
     of the form in this view.
    """
    # TODO: Determine best implementation of this
    def get_form(self, *args, **kwargs):
        form = super().get_form(*args, **kwargs)

        form.instance.owner = UserProfile.objects.get(user=self.request.user)
        return form

    # def get_form_kwargs(self):
    #     kwargs = super().get_form_kwargs()
    #     # Update the forms kwargs with the current UserProfile
    #     # kwargs['instance'].owner = UserProfile.objects.get(user=self.request.user)
    #     # kwargs.update({'owner': UserProfile.objects.get(user=self.request.user)})
    #     return kwargs
    #
    # def form_valid(self, form):
    #     form.instance.owner = UserProfile.objects.get(user=self.request.user)
    #     return super().form_valid(form)


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
