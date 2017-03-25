from allauth.socialaccount.providers.oauth2.urls import default_urlpatterns

from .provider import QqProvider


urlpatterns = default_urlpatterns(QqProvider)
