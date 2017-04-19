# 创 建 人：张太红
# 创建日期：2017年04月19日

from django.contrib import admin
from .models import Languages


class LanguagesAdmin(admin.ModelAdmin):
    list_display = ('localeCode', 'languageName')  # 列表

# 注册Languages模型，以便Django Admin可以直接维护该表的数据
admin.site.register(Languages, LanguagesAdmin)
