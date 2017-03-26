from allauth.socialaccount.providers.base import ProviderAccount
from allauth.socialaccount.providers.oauth2.provider import OAuth2Provider
from django.utils.translation import ugettext_lazy as _
from urllib.parse import unquote  # url解码


class TaobaoAccount(ProviderAccount):
    def to_str(self):
        return self.account.extra_data.get(
            'uname',
            super(TaobaoAccount, self).to_str())


class TaobaoProvider(OAuth2Provider):
    id = 'taobao'
    name = _('Taobao')
    account_class = TaobaoAccount

    def extract_uid(self, data):
        # return data.get('taobao_user_id')
        return data['response']['taobao_user_id']

    def extract_common_fields(self, data):
        uid = data['response']['taobao_user_id']
        nick = data['response']['taobao_user_nick']
        uname = data['response']['taobao_user_nick']
        # return dict(uid=data.get('taobao_user_id'), username=data.get('taobao_user_nick'), uname=data.get('taobao_user_nick'))
        return dict(uid=data['response']['taobao_user_id'],
                    username=unquote(data['response']['taobao_user_nick']),
                    uname=unquote(data['response']['taobao_user_nick']))


provider_classes = [TaobaoProvider]
