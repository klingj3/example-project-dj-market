from django import forms

from market.apps.core.mixins import CreateWithOwnerMixin
from market.apps.social.models import UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['name', 'organization_name', 'bio', 'location', 'public_email', 'public_website', 'social_url']
        # labels ={
        #     'name':"Your Name",
        #     'organization_name':"Your Organization's Name",
        #     'bio':"Bio - What should your buyers know?",
        #     'public_email':"Public Email",
        #     'public_website':"Website",
        #     'social_url':"Customize your url! [websiteurl]/sellers/...",
        # }

    # Avatar cleaning code taken from here https://stackoverflow.com/questions/6396442/add-image-avatar-field-to-users-in-django
    # def clean_avatar(self):
    #     avatar = self.cleaned_data['avatar']
    #
    #     try:
    #         w, h = get_image_dimensions(avatar)
    #
    #         #validate dimensions
    #         max_width = max_height = 100
    #         if w > max_width or h > max_height:
    #             raise forms.ValidationError(
    #                 u'Please use an image that is '
    #                  '%s x %s pixels or smaller.' % (max_width, max_height))
    #
    #         #validate content type
    #         main, sub = avatar.content_type.split('/')
    #         if not (main == 'image' and sub in ['jpeg', 'pjpeg', 'gif', 'png']):
    #             raise forms.ValidationError(u'Please use a JPEG, '
    #                 'GIF or PNG image.')
    #
    #         #validate file size
    #         if len(avatar) > (3000 * 1024):
    #             raise forms.ValidationError(
    #                 u'Avatar file size may not exceed 3 Mb.')
    #
    #     except AttributeError:
    #         """
    #         Handles case when we are updating the user profile
    #         and do not supply a new avatar
    #         """
    #         pass
    #
    #     return avatar


class UserProfileEditForm(CreateWithOwnerMixin, forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['name', 'organization_name', 'bio', 'location', 'public_email', 'public_website']
        # labels ={
        #     'name':"Your Name",
        #     'organization_name':_("Your Organization's Name"),
        #     'bio':_("Bio - What should your buyers know?"),
        #     'public_email':_("Public Email"),
        #     'public_website':_("External Website"),
        # }
