import requests
import datetime
import hashlib

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
    profile_url = 'https://eco.api.taobao.com/router/rest'




    def complete_login(self, request, app, token, **kwargs):
        """
        secret = 'dca00573f06c81615171ddc6789fc3e8'
        # 淘宝api请求参数
        parameters = {}

        parameters['method'] = 'taobao.user.get'
        parameters['session'] = token.token
        parameters['timestamp'] = datetime.datetime.now().strftime("%Y-%m-%d %X")
        parameters['format'] = 'json'
        parameters['app_key'] = '23717023'
        parameters['v'] = '2.0'
        parameters['sign_method'] = 'md5'
        keys = list(parameters.keys())
        keys.sort()

        sign = "%s%s%s" % (secret,
            str().join('%s%s' % (key, parameters[key]) for key in keys),
            secret)
        sign = sign.encode('utf-8')
        sign = hashlib.md5(sign).hexdigest().upper()
        parameters['sign'] = sign


        resp = requests.get(self.profile_url,params=parameters)
        """
        extra_data = kwargs
        print(extra_data)
        return self.get_provider().sociallogin_from_response(request,extra_data)


oauth2_login = OAuth2LoginView.adapter_view(TaobaoOAuth2Adapter)
oauth2_callback = OAuth2CallbackView.adapter_view(TaobaoOAuth2Adapter)
