# 创 建 人：张太红
# 创建日期：2017年04月12日

from django.db import models
from django.contrib.auth.models import User


class Languages(models.Model):
    """
    zh-hans, 简体中文
    en-us,   English
    ug-ar,   ئۇيغۇر تىلى‎
    kk-ar,   قازاق ٴتىلى
    """

    localeCode =  models.CharField(max_length=10, primary_key=True)   # 语言代码
    languageName = models.TextField(max_length=30, blank=False)       # 语言名称


class UserProfile(models.Model):
    user = models.ForeignKey(User, unique=True)                        # 用户ID
    userName = models.CharField(max_length=30, blank=True)             # 真实姓名
    localeCode = models.ForeignKey(Languages)                          # 偏好语言代码
    mobile = models.CharField(max_length=15)                           # 手机号码
    mobileVerified = models.BooleanField(default=False, blank=False)   # 手机号码是否通过短信验证
    address = models.TextField(max_length=200)                         # 通讯地址



User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])
