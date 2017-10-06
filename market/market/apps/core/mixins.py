from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        UserPassesTestMixin)


class CreateWithOwnerMixin(LoginRequiredMixin):
    def get_form(self, form_class=None):
        # Inject the logged in user into the form
        form = super(CreateByUserMixin, self).get_form(form_class)
        form.instance.user = self.request.user

        return form


class UserIsOwnerMixin(UserPassesTestMixin): #, SingleObjectMixin):
    def test_func(self):
        return self.request.user == self.get_object().owner
