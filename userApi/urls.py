from django.conf.urls import url, include
from rest_framework import routers
from . views import UserView, currentUser, currentUserProfile

router = routers.DefaultRouter()
router.register(r'users', UserView, 'list')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^api/getUserInfo', currentUser, name = 'userInfo'),
    url(r'^api/getUserProfile', currentUserProfile.as_view(), name = 'userProfile'),
]
