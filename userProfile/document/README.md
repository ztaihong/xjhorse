# userProfile（个人资料） App 开发详细过程

## 一、创建App
在命令行进行以下三部操作即可创建一个名称为userProfile的Django应用：
##### 1、激活虚拟环境
    source xjhorse_venv/bin/activate
##### 2、转入项目目录
    cd /Users/zhangtaihong/PycharmProjects/xjhorse/
##### 3、创建userProfile应用
    python manage.py startapp userProfile
在Pycharm集成开发环境则只需进行以下两部操作即可创建一个名称为userProfile的Django应用：

##### 1、在Pycharm的【Tools】菜单选择【Run manage.py Task...】
##### 2、在manage.py命令行创建userProfile应用
    startapp userProfile

## 二、创建Model

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
        
        localeCode =  models.CharField(max_length=10, primary_key=True, verbose_name=_("Language Code"))   # 语言代码, 不使用自动主键
        languageName = models.TextField(max_length=30, blank=False, verbose_name=_("Language name"))       # 语言名称    
        
    # 每个注册用户的个人附加信息
    class UserProfile(models.Model):
        user = models.OneToOneField(User, primary_key=True)                # 用户ID, 不使用自动主键
        userName = models.CharField(max_length=30, blank=True)             # 真实姓名
        localeCode = models.ForeignKey(Languages)                          # 偏好语言代码
        mobile = models.CharField(max_length=15)                           # 手机号码
        mobileVerified = models.BooleanField(default=False, blank=False)   # 手机号码是否通过短信验证
        address = models.TextField(max_length=200)                         # 通讯地址
        
    User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])
## 三、使用Model
修改项目的settings.py文件，添加以下内容：

    INSTALLED_APPS = [
   
        # 用户个人资料App，目前主要为了让用户能够选择自己偏好的语言
        'userProfile',
        #...
    ]
    
## 四、创建表

    manage.py makemigrations userProfile
    manage.py migrate userProfile
## 五、注册Languages模型，以便Django Admin可以直接维护该表的数据
编辑userProfile应用的admin.py文件，添加以下内容：

    from django.contrib import admin
    from .models import Languages
    class LanguagesAdmin(admin.ModelAdmin):
        list_display = ('localeCode', 'languageName')  # 列表显示

    # 注册Languages模型，以便Django Admin可以直接维护该表的数据
    admin.site.register(Languages, LanguagesAdmin)
    
## 六、App名称及多语言支持
编辑userProfile应用的apps.py文件，添加以下内容：

    from django.apps import AppConfig
    from django.utils.translation import ugettext_lazy as _
      
    class UserprofileConfig(AppConfig):
        name = 'userProfile'
        verbose_name = _('User Profile')
        
        
编辑userProfile应用的__init__.py文件，添加以下内容：

    default_app_config = 'userProfile.apps.UserprofileConfig'
    

在userProfile应用中创建locale目录，然后运行以下命令生成要翻译的信息表：

    manage.py makemessages --locale zh_Hans --locale ug_Ar --locale kk_Ar --no-wrap --domain django
    
翻译locale目录下kk_Ar、ug_Ar、zh_Hans目录中LC_MESSAGES子目录中django.po信息文件，然后运行下列命令编译翻译的信息：

    manage.py compilemessages
