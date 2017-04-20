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
编辑userProfile应用models.py文件，添加以下内容：

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
        address = models.TextField(max_length=200, verbose_name=_("Address"))                                 # 通讯地址
        
        def get_language(self):
            return self.localeCode

## 三、使用Model
修改项目的settings.py文件，添加以下内容：

    INSTALLED_APPS = [
   
        # 用户个人资料App，目前主要为了让用户能够选择自己偏好的语言
        'userProfile',
        #...
    ]
    
## 四、通过Model创建表

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
    
    
## 六、访问Django管理界面
通过浏览器访问http://www.xjhorse.net:8000/admin/  

点击【用户资料】→【偏好语言】，将以下四条记录添加到数据库中：

    zh-hans, 简体中文
    en-us,   English
    ug-ar,   ئۇيغۇر تىلى‎
    kk-ar,   قازاق ٴتىلى
        
## 七、App名称及多语言支持
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

## 八、创建基于Model的Form
编辑userProfile应用的forms.py文件，添加以下内容：

    from django.forms import ModelForm, Textarea, TextInput
    from . models import UserProfile
    
    class UserProfileForm(ModelForm):
        class Meta:
            model = UserProfile
            fields = ('user', 'userName', 'localeCode', 'mobile', 'mobileVerified', 'address')
            widgets = {
                'address': Textarea(attrs={'cols': 80, 'rows': 1}),
                'user':   TextInput(attrs={'readonly': 'readonly'}),
            }

## 九、创建模板
在userProfile应用中创建templates目录，然后在templates目录再创建userProfile子目录
#### 1、在上述子目录创建userProfile.html模板文件，用于布局"用户资料"的编辑界面，内容如下：

    {% extends "bootstrap/bootstrap.html" %}
    
    {% load i18n %}
    {% load bootstrap3 %}
    
    {% block head_title %}{% trans "User Profile" %}{% endblock %}
    
    {% block inner-content %}
        <h1>{% trans "User Profile" %}</h1>
        <hr>
    
        <form method="post" action="">
            {% csrf_token %}
            {% bootstrap_form form %}
            <button type="submit">{% trans 'Submit' %}</button>
        </form>
    
    
    {% endblock %}
#### 2、在上述子目录创建success.html模板文件，用于布局"用户资料"的展示界面，内容如下：
    {% extends "bootstrap/bootstrap.html" %}
    
    {% load i18n %}
    
    
    {% block head_title %}{% trans "User Profile" %}{% endblock %}
    
    {% block inner-content %}
        <h1>{% trans "User Profile" %}</h1>
        <hr>
        <table width="100%" border="2">
            <tr>
                <td width="30%">{% trans "UserID" %}</td>
                <td>{{ profile.user }}</td>
            </tr>
            <tr>
                <td>{% trans "User Name" %}</td>
                <td>{{ profile.userName }}</td>
            </tr>
            <tr>
                <td>{% trans "Language" %}</td>
                <td>{{ profile.localeCode }}</td>
            </tr>
            <tr>
                <td>{% trans "Mobile" %}</td>
                <td>{{ profile.mobile }}</td>
            </tr>
            <tr>
                <td>{% trans "Mobile Verified" %}</td>
                <td>{{ profile.mobileVerified }}</td>
            </tr>
            <tr>
                <td>{% trans "Address" %}</td>
                <td>{{ profile.address }}</td>
            </tr>
    
        </table>
    
    {% endblock %}
    
## 十、创建视图
编辑userProfile应用的views.py文件，添加以下内容：

    from . models import UserProfile
    from . forms import UserProfileForm
    from django.views.generic.edit import UpdateView
    from django.utils.translation import LANGUAGE_SESSION_KEY
    from django.contrib.auth.mixins import LoginRequiredMixin
    from django.contrib.auth.decorators import login_required
      
    # 创建基于Form的视图，用于编辑"用户资料"
    # 提交后将修改结果保存到数据库，同时通过session设置偏好语言
    
    class UserProfileView(LoginRequiredMixin, UpdateView):
        template_name = 'userProfile/userProfile.html'
        success_url = 'success'
        form_class = UserProfileForm
        model = UserProfile
        
        # 如果登录的用户存在"用护资料"记录，直接获取之，否则创建一条记录
        def get_object(self, queryset=None):
            profile = None
            try:
                profile = self.model.objects.get(user=self.request.user)
            except UserProfile.DoesNotExist:
                profile = UserProfile(user = self.request.user)
            return profile
        
        # 保存记录到数据库之前，先通过session设置偏好语言
        def form_valid(self, form):
            self.object = form.save(commit=False)
            language = self.object.get_language()
            self.request.session[LANGUAGE_SESSION_KEY] = language.localeCode
            self.object.save()
    
            return super(UserProfileView, self).form_valid(form)
    
      
    # 创建基于函数的视图，用于展示"用户资料"提交成功的界面
    from django.http import HttpResponse
    from django.template import loader
    @login_required
    def success(request):
        profile = UserProfile.objects.get(user = request.user)
        template = loader.get_template('userProfile/success.html')
        context = {
            'profile': profile,
        }
        return HttpResponse(template.render(context, request))

## 十一、设置url导航规则
在userProfile应用中创建urls.py文件，添加以下内容：

    from django.conf.urls import url
    from . views import UserProfileView, success
    
    urlpatterns = [
        url(r'^profile/$', UserProfileView.as_view(), name='profile'),
        url(r'^profile/success$', success, name='success'),
    ]

## 十二、测试
1、在PyCHarm运行xjhorse  
2、通过浏览器访问http://www.xjhorse.net:8000
