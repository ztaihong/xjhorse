"""
xjhorse URL 配置

urlpatterns列表用来将URLs路由到对应的视图。
详细情况请参阅：https://docs.djangoproject.com/en/1.10/topics/http/urls/

例如:
函数视图
    from my_app import views                   # 从my_app导入views
    url(r'^$', views.home, name='home')        # 将一个URL添加到urlpatterns

类视图
    from other_app.views import Home           # 从other_app.views导入Home
    url(r'^$', Home.as_view(), name='home')    # 将一个URL添加到urlpatterns
    
包含其它URL配置文件
    from django.conf.urls import url, include  # 从django.conf.urls导入url, include函数
    url(r'^blog/', include('blog.urls'))       # 将一个URL配置文件添加到urlpatterns
"""
from django.conf.urls import url, include # Add include to the imports here
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [

    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('allauth.urls')),                                     # allauth第三方认证账户管理
    url(r'^', include('homePage.urls')),                                             # 读入homePage app中的urls.py
    url(r'^', include('userProfile.urls')),                                          # 读入userProfile app中的urls.py
    url(r'^oauth2/', include('oauth2_provider.urls', namespace='oauth2_provider')),  # oauth2 urls
    url(r'^', include('userApi.urls')),                                              # 读入userApi app中的urls.py
]

urlpatterns += staticfiles_urlpatterns()                                             # 处理静态文件