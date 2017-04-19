from django.conf.urls import url
from . views import UserProfileView

urlpatterns = [
    url(r'^profile/$', UserProfileView.as_view(), name='profile'),
]
