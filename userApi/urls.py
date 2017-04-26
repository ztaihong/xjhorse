from django.conf.urls import url, include
from rest_framework import routers
from . views import UserView, current_user

router = routers.DefaultRouter()
router.register(r'users', UserView, 'list')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^api/getUserInfo', current_user, name = 'userInfo'),
]
