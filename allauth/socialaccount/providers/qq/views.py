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

    # OpenID是此网站上或应用中唯一对应用户身份的标识，
    # 网站或应用可将此ID进行存储，便于用户下次登录时辨识其身份，
    # 或将其与用户在网站上或应用中的原有账号进行绑定。
    OpenID_url = 'https: // graph.qq.com/oauth2.0/me'

    # 获取登录用户的昵称、头像、性别
    profile_url = 'https://graph.qq.com/user/get_user_info'

    def complete_login(self, request, app, token, **kwargs):
        resp = requests.get(self.profile_url,
                            params={'access_token': token.token})
        extra_data = resp.json()
        return self.get_provider().sociallogin_from_response(request,
                                                             extra_data)


oauth2_login = OAuth2LoginView.adapter_view(QqOAuth2Adapter)
oauth2_callback = OAuth2CallbackView.adapter_view(QqOAuth2Adapter)
