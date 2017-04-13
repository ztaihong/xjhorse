# 创 建 人：张太红
# 创建日期：2017年04月12日

from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.ForeignKey(User, unique=True)
    userName = models.CharField(max_length=30, blank=True)
    


User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])
