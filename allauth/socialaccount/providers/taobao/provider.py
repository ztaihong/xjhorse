from allauth.socialaccount.providers.base import ProviderAccount
from allauth.socialaccount.providers.oauth2.provider import OAuth2Provider


class TaobaoAccount(ProviderAccount):



    def to_str(self):
        return self.account.extra_data.get(
            'uname',
            super(TaobaoAccount, self).to_str())


class TaobaoProvider(OAuth2Provider):
    id = 'taobao'
    name = 'Taobao（淘宝）'
    account_class = TaobaoAccount

    def extract_uid(self, data):
        return data['uid']


    def extract_common_fields(self, data):
        return dict(username=data.get('uid'),
                    name=data.get('uname'))


provider_classes = [TaobaoProvider]
