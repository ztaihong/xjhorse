from django.forms import ModelForm, Textarea, TextInput
from . models import UserProfile

class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ('user', 'userName', 'localeCode', 'mobile', 'mobileVerified', 'address')
        widgets = {
            'address': Textarea(attrs={'cols': 80, 'rows': 1}),
            'user':   TextInput(attrs={'readonly': 'readonly'}),
        }
