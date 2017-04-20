# 创 建 人：张太红
# 创建日期：2017年04月12日

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
