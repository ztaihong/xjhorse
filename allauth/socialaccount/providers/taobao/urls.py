from allauth.socialaccount.providers.oauth2.urls import default_urlpatterns

from .provider import TaobaoProvider


urlpatterns = default_urlpatterns(TaobaoProvider)
