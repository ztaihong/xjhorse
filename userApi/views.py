# 创 建 人：张太红
# 创建日期：2017年04月26日

from django.contrib.auth.models import User
from django.http import HttpResponse
from rest_framework import permissions, viewsets
from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView

from oauth2_provider.ext.rest_framework import TokenHasScope
from . serializers import UserSerializer, UserInfoSerializer
from . permissions import IsStaffOrTargetUser

@api_view(['GET'])
class CurrentUserView(APIView):
    permission_classes = [permissions.IsAuthenticated, TokenHasScope]
    required_scopes = ['read']
    def get(self, request):
        serializer = UserInfoSerializer(request.user)
        return HttpResponse(serializer.data)


class UserView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    model = User

    def get_permissions(self):
        # 允许非认证访问者通过POST创建一个用户
        if self.request.method == 'POST':
            return AllowAny()
        else:
            return IsStaffOrTargetUser()
