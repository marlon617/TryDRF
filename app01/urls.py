#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
-----------------------------------------
@author: Marlon617
@contact: malong617@163.com
@software: PyCharm
@file: urls.py
@time: 2019/4/28 4:09 PM
-----------------------------------------
"""

from django.urls import path,include
from . import views

urlpatterns = [
    path('publishers/', views.publisher_list),
]
