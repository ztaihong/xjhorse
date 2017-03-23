import requests

from allauth.socialaccount.providers.oauth2.views import (
    OAuth2Adapter,
    OAuth2CallbackView,
    OAuth2LoginView,
)

from .provider import TaobaoProvider


class TaobaoOAuth2Adapter(OAuth2Adapter):
    provider_id = TaobaoProvider.id
    access_token_url = 'https://oauth.taobao.com/token'
    authorize_url = 'https://oauth.taobao.com/authorize'
    profile_url = 'https:taobao.open.account.search'


    def complete_login(self, request, app, token, **kwargs):
        resp = requests.get(self.profile_url,
                            params={'access_token': token.token})
        extra_data = resp.json()

        return self.get_provider().sociallogin_from_response(request,
                                                             extra_data)


oauth2_login = OAuth2LoginView.adapter_view(TaobaoOAuth2Adapter)
oauth2_callback = OAuth2CallbackView.adapter_view(TaobaoOAuth2Adapter)
