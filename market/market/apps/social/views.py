from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Avg
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import (DetailView,
                                  FormView,
                                  ListView,
                                  RedirectView,
                                  UpdateView)
from extra_views import (CreateWithInlinesView)
from market.apps.board.models import Post
from market.apps.core.mixins import (CreateWithOwnerMixin,
                                     CreateWithReviewerMixin,
                                     CreateWithSenderMixin,
                                     OwnerRequiredMixin,
                                     SellerRequiredMixin)
from market.apps.core.models import UserProfile
from market.apps.social.forms import (ReviewForm,
                                      SocialProfileUpdateForm,)
from market.apps.social.models import (Review,
                                       SocialProfile,)


# Create a new Review
class ReviewCreateView(CreateWithReviewerMixin, CreateWithInlinesView):
    model = Review
    form_class = ReviewForm
    template_name = 'social/review_form.html'

    def get_form(self, form_class):
        form = super().get_form(ReviewForm)
        reviewee = UserProfile.objects.filter(slug=self.kwargs['slug'])
        if len(reviewee) > 0:
            form.fields['reviewee'].queryset = reviewee
        else:
            raise Http404("Invalid Reviewee attempted.")
        return form

    def get_success_url(self):
        messages.success(self.request, 'Review posted!', extra_tags='fa fa-check')
        return reverse('board:list')

#TODO: ReviewUpdateView

# View a single review. Currently, this isn't part of the site, but may be used later
# if, for example, review subjects can respond to a review.
class ReviewDetailView(DetailView):
    model = Review
    template_name = 'social/review_detail.html'

# Viewing a seller's own profile
class SocialProfileSelfDetailView(SellerRequiredMixin, DetailView):
    model = SocialProfile
    context_object_name = 'social_profile'
    template_name = 'social/profile_detail.html'

    def get_object(self, *args, **kwargs):
        return SocialProfile.objects.get(owner=self.request.profile)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts_list'] = Post.objects.filter(owner=self.request.profile).order_by("-modified")
        context['reviews_list'] = Review.objects.filter(reviewee=self.request.profile).order_by("-modified")
        if len(context['reviews_list']) > 0:
            average = context['reviews_list'].aggregate(Avg('score'))['score__avg']
        else:
            average = 0
        average_str = []
        val = 0.00
        ''' Django HTML has a hard time looping through numerical values, so to display the score
        we convert it to a string, (5 stars is 'fffff', 0 is 'eeeee') and then iterate through the
        string to display stars on a seller's page. Hacky to be sure, but I wasn't able to find a
        more elegant alternative'''
        while val < 5:
            if val + 1 <= average:
                average_str.append('f')
            elif val + 0.5 <= average:
                average_str.append('h')
            else:
                average_str.append('e')
            val += 1
        context['average_str'] = average_str
        context['average'] = average
        return context

# Same as the above, but for viewing another seller.
class SocialProfileDetailView(DetailView):
    model = SocialProfile
    context_object_name = 'social_profile'
    template_name = 'social/profile_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = SocialProfile.objects.get(slug=self.kwargs['slug']).owner
        context['posts_list'] = Post.objects.filter(owner=user).order_by("-modified")
        context['reviews_list'] = Review.objects.filter(reviewee=user).order_by("-modified")
        if len(context['reviews_list']) > 0:
            average = context['reviews_list'].aggregate(Avg('score'))['score__avg']
        else:
            average = 0
        average_str = []
        val = 0.00
        while val < 5:
            if val + 1 <= average:
                average_str.append('f')
            elif val + 0.5 <= average:
                average_str.append('h')
            else:
                average_str.append('e')
            val += 1
        context['average_str'] = average_str
        context['average'] = average
        return context

# Update a profile.
class SocialProfileUpdateView(SellerRequiredMixin, OwnerRequiredMixin, UpdateView):
    model = SocialProfile
    form_class = SocialProfileUpdateForm
    template_name = 'social/profile_update_form.html'

    def get_object(self, *args, **kwargs):
        return SocialProfile.objects.get(owner=self.request.profile)

    def get_success_url(self):
        messages.success(self.request, 'Seller profile updated!', extra_tags='fa fa-check')
        return reverse('social:update')
