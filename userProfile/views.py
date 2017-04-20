from django.shortcuts import render
from . models import UserProfile
from . forms import UserProfileForm
from django.views.generic.edit import UpdateView
from django.utils.translation import LANGUAGE_SESSION_KEY
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.

class UserProfileView(LoginRequiredMixin, UpdateView):
    template_name = 'userProfile/userProfile.html'
    success_url = 'success'
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
        language = self.object.get_language()
        self.request.session[LANGUAGE_SESSION_KEY] = language.localeCode
        self.object.save()

        return super(UserProfileView, self).form_valid(form)



from django.http import HttpResponse
from django.template import loader


@login_required
def success(request):
    profile = UserProfile.objects.get(user = request.user)
    template = loader.get_template('userProfile/success.html')
    context = {
        'profile': profile,
    }
    return HttpResponse(template.render(context, request))
