# 创 建 人：张太红
# 创建日期：2017年04月12日

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

# 本平台支持的语言
class Languages(models.Model):
    # 目前我们只支持简体中文、英文、维吾尔文和哈萨克文4中语言，所以该表只用以下4条记录：
    """
    zh-hans, 简体中文
    en-us,   English
    ug-ar,   ئۇيغۇر تىلى‎
    kk-ar,   قازاق ٴتىلى
    """

    localeCode =  models.CharField(max_length=10, primary_key=True, verbose_name=_("Language Code"))   # 语言代码, 不适用自动主键
    languageName = models.TextField(max_length=30, blank=False, verbose_name=_("Language name"))       # 语言名称

    class Meta:
        verbose_name = _('Language')
        verbose_name_plural = _('Languages')

    def __str__(self):
        return self.languageName + "（" + self.localeCode + "）"

# 每个注册用户的个人附加信息
class UserProfile(models.Model):
    user = models.OneToOneField(User, primary_key=True, verbose_name=_("UserID"))                         # 用户ID, 不适用自动主键
    userName = models.CharField(max_length=30, blank=True, verbose_name=_("User Name"))                   # 真实姓名
    localeCode = models.ForeignKey(Languages, verbose_name=_("Language"))                                 # 偏好语言代码
    mobile = models.CharField(max_length=15, verbose_name=_("Mobile"))                                    # 手机号码
    mobileVerified = models.BooleanField(default=False, blank=False, verbose_name=_("Mobile Verified"))   # 手机号码是否通过短信验证
    address = models.TextField(max_length=200, verbose_name=_("Address"))
    # 通讯地址

    def get_language(self):
        return self.localeCode
