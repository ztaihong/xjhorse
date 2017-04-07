from allauth.socialaccount.providers.base import ProviderAccount
from allauth.socialaccount.providers.oauth2.provider import OAuth2Provider
from django.utils.translation import ugettext_lazy as _

class QqAccount(ProviderAccount):
    def get_profile_url(self):
        return ('https://graph.qq.com/user/get_user_info')


    def to_str(self):
        dflt = super(QqAccount, self).to_str()
        return self.account.extra_data.get('uname', dflt)


class QqProvider(OAuth2Provider):
    id = 'qq'
    name = _('QQ')
    account_class = QqAccount

    def get_default_scope(self):
        return ['get_user_info']

    def extract_uid(self, data):
        return data['uid']

    def extract_common_fields(self, data):
        return dict(username=data.get('nickname'),uname=data.get('nickname'))


provider_classes = [QqProvider]
