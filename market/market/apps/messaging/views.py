from django.contrib import messages
from django.http import Http404
from django.urls import reverse
from django.views.generic import (DeleteView,
                                  DetailView,
                                  ListView,
                                  TemplateView)

from extra_views import (CreateWithInlinesView,
                         InlineFormSet,
                         UpdateWithInlinesView)
                         
from market.apps.messaging.forms import (MessageForm)
from market.apps.board.models import (Post)
from market.apps.core.mixins import (CreateWithSenderMixin,
                                     OwnerRequiredMixin,
                                     SellerRequiredMixin)
from market.apps.core.models import UserProfile
from market.apps.messaging.models import (Message)
                                     
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
    
class MessageListView(ListView):
    model = Message
    template_name = 'messaging/message_list.html'
    paginate_by = 16