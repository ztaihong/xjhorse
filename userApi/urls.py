from django.conf.urls import url, include
from rest_framework import routers
from . views import UserView, CurrentUserView

router = routers.DefaultRouter()
router.register(r'getUserInfo', CurrentUserView, 'userInfo')
router.register(r'users', UserView, 'list')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^oauth2/', include('oauth2_provider.urls', namespace='oauth2_provider')),
]
