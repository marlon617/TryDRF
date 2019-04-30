#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
-----------------------------------------
@author: Marlon617
@contact: malong617@163.com
@software: PyCharm
@file: serializers.py
@time: 2019/4/28 4:48 PM
-----------------------------------------
"""

from rest_framework import serializers
from app01 import models

#自定义序列化类
# class PublisherSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(max_length=32)
#     address = serializers.CharField(max_length=128)
#
#     #重写创建方法
#     def create(self, validataed_data):
#         return models.Publisher.objects.create(**validataed_data)
#
#     # 重写update方法
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get("name", instance.name)
#         instance.address = validated_data.get("address", instance.address)
#         instance.save()
#         return instance


class PublisherSerializer(serializers.ModelSerializer):
    operator = serializers.ReadOnlyField(source='operator.username')

    class Meta:
        model = models.Publisher
        fields = (
            "id",
            "name",
            "address",
            "operator"
        )

# class BookSerializer(serializers.ModelSerializer):
#     publisher = serializers.StringRelatedField(source="publisher.name")
#
#     class Meta:
#         model = models.Book
#         fields = (
#             "id",
#             "title",
#             "publisher"
#         )

#超链接
class BookSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = models.Book
        fields = (
            "id",
            "title",
            "publisher"
        )