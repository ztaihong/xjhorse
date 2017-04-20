# 创 建 人：张太红
# 创建日期：2017年04月12日

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
