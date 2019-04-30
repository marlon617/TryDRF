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
from django.conf.urls import url
from django.urls import path,include
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^publishers/$', views.publisher_list),
    url(r'^publishers/(?P<pk>[0-9]+)$', views.publisher_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)