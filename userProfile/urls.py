from django.conf.urls import url
from . views import UserProfileView, success

urlpatterns = [
    url(r'^profile/$', UserProfileView.as_view(), name='profile'),
    url(r'^profile/success$', success, name='success'),
]
