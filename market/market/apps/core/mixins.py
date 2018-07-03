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

class CreateWithReviewerMixin(LoginRequiredMixin):
    """
    Injects the currently logged in user to the 'reviewer' field
     of the form in this view.
    """
    def get_form(self, *args, **kwargs):
        form = super().get_form(*args, **kwargs)
        form.instance.reviewer = UserProfile.objects.get(user=self.request.user)
        return form


class CreateWithSenderMixin(LoginRequiredMixin):
    """
    Injects the currently logged in user to the 'sender' field
     of the form in this view.
    """
    # TODO: Determine best implementation of this
    def get_form(self, *args, **kwargs):
        form = super().get_form(*args, **kwargs)

        form.instance.sender = UserProfile.objects.get(user=self.request.user)
        return form


class OwnerRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    """
    Restricts access to this view to the user who is the owner
    of this object (in a single object view).
    """
    # TODO: Raise 404 instead of 503
    raise_exception = True

    def test_func(self):
        # Assumes this has a get_object attribute
        # Could test with hasattr()?
        return self.request.profile == self.get_object().owner


class SellerRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    """
    Resstricts access to this view to users in the Seller group.
    """
    # TODO: Raise 404 instead of 503
    raise_exception = True

    def test_func(self):
        # TODO: Use user groups instead
        # return self.request.user.groups.filter(name='Seller').exists()
        return self.request.profile.is_seller
