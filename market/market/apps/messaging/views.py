from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.urls import reverse
from django.views.generic import (DetailView,
                                  ListView,)

from extra_views import (CreateWithInlinesView)

from market.apps.core.mixins import (CreateWithSenderMixin,
                                     OwnerRequiredMixin,
                                     SellerRequiredMixin)
from market.apps.core.models import UserProfile
from market.apps.messaging.forms import (MessageForm)
from market.apps.messaging.models import (Message)
from market.apps.social.models import SocialProfile

class MessageCreateView(CreateWithSenderMixin, CreateWithInlinesView):
    model = Message
    form_class = MessageForm
    template_name = 'messaging/message_form.html'

    def get_form(self, form_class):
        form = super().get_form(MessageForm)
        recipient = UserProfile.objects.filter(slug=self.kwargs['slug'])
        print(recipient)
        if len(recipient) > 0:
            form.fields['recipient'].queryset = recipient
        else:
            raise Http404("Invalid recipient attempted.")
        return form

    def get_success_url(self):
        messages.success(self.request, 'Message sent!', extra_tags='fa fa-check')
        return reverse('messaging:inbox')

class MessageDetailView(DetailView):
    model = Message
    template_name = 'messaging/message_detail.html'

    # Get's the communicator's social profile, if a seller.
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        message = Message.objects.get(slug=self.kwargs['slug'])
        # If the message is for us, grab profile for the sender, otherwise the recipient
        if message.recipient == self.request.profile:
            context['in_inbox'] = True
            context['social_slug'] = (SocialProfile.objects.get(owner=message.sender)).slug
        else:
            context['in_inbox'] = False
            context['social_slug'] = (SocialProfile.objects.get(owner=message.recipient)).slug
        return context

    
class MessageListView(LoginRequiredMixin, ListView):
    model = Message
    template_name = 'messaging/message_list.html'
    paginate_by = 16

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['outbox'] = Message.objects.filter(sender=self.request.profile).order_by('-created')
        context['inbox'] = Message.objects.filter(recipient=self.request.profile).order_by('-created')
        return context