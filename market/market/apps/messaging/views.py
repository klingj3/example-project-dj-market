from django.contrib import messages
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
from market.apps.messaging.models import (Message)
                                     
class MessageCreateView(CreateWithSenderMixin, CreateWithInlinesView):
    model = Message
    form_class = MessageForm
    template_name = 'messaging/message_form.html'
    
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