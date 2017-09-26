from django.contrib.auth.mixins import LoginRequiredMixin

class CreateByUserMixin(LoginRequiredMixin):
    def get_form(self, form_class=None):
        # Inject the logged in user into the form
        form = super(CreateByUserMixin, self).get_form(form_class)
        form.instance.user = self.request.user

        return form