# 创 建 人：张太红
# 创建日期：2017年04月26日

from django.contrib.auth.models import User
from django.http import JsonResponse
from rest_framework import permissions, viewsets
from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny
from rest_framework import generics
from oauth2_provider.ext.rest_framework import TokenHasReadWriteScope
from . serializers import UserSerializer, UserProfileSerializer
from . permissions import IsStaffOrTargetUser
from userProfile.models import UserProfile


@api_view(['GET'])
def currentUser(request):
    user = request.user
    return JsonResponse({
        'username': user.username,
        'email': user.email
    })

@api_view(['GET'])
def currentUserProfile(request):
    user = request.user
    return JsonResponse({
        'username': user.username,
        'email': user.email
    })

class currentUserProfile(generics.ListAPIView):
    serializer_class = UserProfileSerializer

    def get_queryset(self):
        #该视图将返回当前登录用户的附加信息

        current_user = self.request.user
        return UserProfile.objects.filter(user=current_user)


class UserView(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    serializer_class = UserSerializer
    queryset = User.objects.all()
    model = User

    def get_permissions(self):
        # 允许非认证访问者通过POST创建一个用户
        return (AllowAny() if self.request.method == 'POST'
                else IsStaffOrTargetUser()),
