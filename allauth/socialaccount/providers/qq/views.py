import requests

from allauth.socialaccount.providers.oauth2.views import (
    OAuth2Adapter,
    OAuth2CallbackView,
    OAuth2LoginView,
)

from .provider import QqProvider


class QqOAuth2Adapter(OAuth2Adapter):
    provider_id = QqProvider.id

    access_token_url = 'https://graph.qq.com/oauth2.0/token'
    authorize_url = 'https://graph.qq.com/oauth2.0/authorize'

    # 获取登录用户的昵称、头像、性别接口地址
    profile_url = 'https://graph.qq.com/user/get_user_info'

    def complete_login(self, request, app, token, **kwargs):
        # 获取openid
        openIdUrl = "https://graph.qq.com/oauth2.0/me"
        openIdUrlResp = requests.get(openIdUrl, params={'access_token': token.token})
        respContent = openIdUrlResp.content.decode("utf-8")
        resultDict = eval(respContent[10:len(respContent) - 3])
        openid = resultDict["openid"]
        clientid = resultDict["client_id"]

        # 获取登录用户的昵称、头像、性别
        resp = requests.get(self.profile_url,
                            params={'access_token': token.token,
                                    'oauth_consumer_key': clientid, 'openid': openid})
        extra_data = resp.json()
        extra_data['uid'] = openid;  # openid是各类腾讯账号的唯一标识
        return self.get_provider().sociallogin_from_response(request,
                                                             extra_data)


oauth2_login = OAuth2LoginView.adapter_view(QqOAuth2Adapter)
oauth2_callback = OAuth2CallbackView.adapter_view(QqOAuth2Adapter)
