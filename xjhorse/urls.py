"""xjhorse URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include # Add include to the imports here
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = [

    url(r'^admin/', admin.site.urls),
    # allauth在django需要以下配置
    url(r'^accounts/', include('allauth.urls')),
    url(r'^', include('homePage.urls')),  # 读入homePage app中的urls.py
]
