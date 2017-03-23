import requests
import datetime

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
    profile_url = 'http://gw.api.taobao.com/router/rest'


    def complete_login(self, request, app, token, **kwargs):
        resp = requests.get(self.profile_url,
                            params={
                                'method': 'taobao.user.get',
                                'fomate': 'json',
                                'v': '2.0',
                                'access_token': token.token,
                                'app_key': '23717023',
                                'timestamp': datetime.datetime.now().strftime("%Y-%m-%d %X"),
                                'sign': 'dca00573f06c81615171ddc6789fc3e8'
                            })
        extra_data = resp.json()
        print(extra_data)

        return self.get_provider().sociallogin_from_response(request,extra_data)


oauth2_login = OAuth2LoginView.adapter_view(TaobaoOAuth2Adapter)
oauth2_callback = OAuth2CallbackView.adapter_view(TaobaoOAuth2Adapter)
