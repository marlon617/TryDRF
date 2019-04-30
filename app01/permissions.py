#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
-----------------------------------------
@author: Marlon617
@contact: malong617@163.com
@software: PyCharm
@file: permissions.py.py
@time: 2019/4/29 4:06 PM
-----------------------------------------
"""

from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    自定义权限只允许对象的所有者编辑它。
    """

    def has_object_permission(self, request, view, obj):
        # 读取权限允许任何请求，
        # 所以我们总是允许GET，HEAD或OPTIONS请求。
        if request.method in permissions.SAFE_METHODS:
            return True

        # 只有该出版社的所有者才允许写权限。
        return obj.operator == request.user