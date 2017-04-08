from allauth.socialaccount.providers.base import ProviderAccount
from allauth.socialaccount.providers.oauth2.provider import OAuth2Provider
from django.utils.translation import ugettext_lazy as _
from urllib.parse import unquote  # url解码


class TaobaoAccount(ProviderAccount):
    def to_str(self):
        dflt = super(TaobaoAccount, self).to_str()
        return unquote(self.account.extra_data['response'].get('taobao_user_nick', dflt))


class TaobaoProvider(OAuth2Provider):
    id = 'taobao'
    name = _('Taobao')
    account_class = TaobaoAccount

    def extract_uid(self, data):
        # return data.get('taobao_user_id')
        return data['response']['taobao_user_id']

    def extract_common_fields(self, data):
        return dict(uid=data['response']['taobao_user_id'],
                    username=unquote(data['response']['taobao_user_nick']),
                    email='无法获取账户Email')


provider_classes = [TaobaoProvider]
