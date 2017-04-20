# 创 建 人：张太红
# 创建日期：2017年04月12日

from django.conf.urls import url
from . views import UserProfileView, success

urlpatterns = [
    url(r'^profile/$', UserProfileView.as_view(), name='profile'),
    url(r'^profile/success$', success, name='success'),
]
