# 创 建 人：张太红
# 创建日期：2017年04月26日

from rest_framework import permissions

class IsStaffOrTargetUser(permissions.BasePermission):
    def has_permission(self, request, view):
        # 如果登录用户为staff，则允许其获取所有用户的列表
        return view.action == 'retrieve' or request.user.is_staff

    def has_object_permission(self, request, view, obj):
        # 允许登录用户查看自己的详细信息，允许staff查看所有用户的详细信息
        return request.user.is_staff or obj == request.user
