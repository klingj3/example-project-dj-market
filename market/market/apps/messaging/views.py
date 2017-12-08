from django.contrib import messages
from django.urls import reverse
from django.views.generic import (DetailView,
                                  ListView,)

from extra_views import (CreateWithInlinesView)

from market.apps.board.models import Post
from market.apps.core.mixins import (CreateWithSenderMixin,
                                     LoginRequiredMixin,
                                     OwnerRequiredMixin,
                                     SellerRequiredMixin)
from market.apps.core.models import UserProfile
from market.apps.messaging.forms import (MessageForm)
from market.apps.messaging.models import (Message)
from market.apps.social.models import SocialProfile


# Create a new message
class MessageCreateView(CreateWithSenderMixin, CreateWithInlinesView):
    model = Message
    form_class = MessageForm
    template_name = 'messaging/message_form.html'

    def get_form(self, form_class):
        form = super().get_form(MessageForm)
        recipient = UserProfile.objects.filter(slug=self.kwargs['slug'])
        if len(recipient) > 0:
            form.fields['recipient'].queryset = recipient
        else:
            raise Http404("Invalid recipient attempted.")
        # Only objects owned by one of the two messengers can be discussed.
        form.fields['referenced_post'].queryset = Post.objects.filter(owner=recipient or self.request.profile).order_by('-modified')
        return form

    def get_success_url(self):
        messages.success(self.request, 'Message sent!', extra_tags='fa fa-check')
        return reverse('messaging:inbox')

# View a single message.
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
            # Other messages involving this person
            context['thread'] = Message.objects.filter(sender=message.sender, recipient=message.sender).order_by("-created")
        else:
            context['in_inbox'] = False
            context['social_slug'] = (SocialProfile.objects.get(owner=message.recipient)).slug
            # Other messages involving this person
            context['thread'] = Message.objects.filter(sender=message.recipient, recipient=message.recipient).order_by("-created")

        return context

# View multiple messages
class MessageListView(LoginRequiredMixin, ListView):
    model = Message
    template_name = 'messaging/message_list.html'
    paginate_by = 16

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['outbox'] = Message.objects.filter(sender=self.request.profile).order_by('-created')
        context['inbox'] = Message.objects.filter(recipient=self.request.profile).order_by('-created')
        return context