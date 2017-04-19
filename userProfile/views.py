from django.shortcuts import render
from . models import UserProfile
from . forms import UserProfileForm
from django.views.generic.edit import UpdateView
from django.utils.translation import LANGUAGE_SESSION_KEY

# Create your views here.

class UserProfileView(UpdateView):
    template_name = 'userProfile/userProfile.html'
    form_class = UserProfileForm
    model = UserProfile

    # That should be all you need. If you need to do any more custom stuff
    # before saving the form, override the `form_valid` method, like this:

    def get_object(self, queryset=None):
        profile = None
        try:
            profile = self.model.objects.get(user=self.request.user)
        except UserProfile.DoesNotExist:
            profile = UserProfile(user = self.request.user)
        return profile

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.request.session[LANGUAGE_SESSION_KEY] = self.object.get_language()
        # Do any custom stuff here

        self.object.save()

        return super(UserProfileView, self).form_valid(form)
