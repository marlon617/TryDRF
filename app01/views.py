
# 类试图
from django.http import Http404


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins
from rest_framework import generics
from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse


from app01 import models
from app01 import serializers
from app01.permissions import IsOwnerOrReadOnly

# 第一种
# class PublisherList(APIView):
#     """
#     列出所有的出版社，或者创建一个新的出版社
#     """
#
#     def get(self, request, format=None):
#         queryset = models.Publisher.objects.all()
#
#         s = serializers.PublisherSerializer(queryset, many=True)
#         return Response(s.data)
#
#     def post(self, request, format=None):
#         s = serializers.PublisherSerializer(data=request.data)
#
#         if s.is_valid():
#             s.save()
#             return Response(s.data, status=status.HTTP_201_CREATED)
#         return Response(s.errors, status=status.HTTP_400_BAD_REQUEST)

# 第二种
# class PublisherList(mixins.ListModelMixin,
#                     mixins.CreateModelMixin,
#                     generics.GenericAPIView):
#
#     queryset = models.Publisher.objects.all()
#     serializer_class = serializers.PublisherSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

#第三种
class PublisherList(generics.ListCreateAPIView):
    queryset = models.Publisher.objects.all()
    serializer_class = serializers.PublisherSerializer
    permission_classes = (IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(operator=self.request.user)

# 第一种
# class PublisherDetail(APIView):
#     """
#     具体的出版社，查看，修改，删除视图
#     """
#     def get_object(self, pk):
#         try:
#             return models.Publisher.objects.get(pk=pk)
#         except models.Publisher.DoesNotExist:
#             raise Http404
#
#
#     # 查看具体的出版社信息
#     def get(self, request, pk, format=None):
#         publisher = self.get_object(pk)
#         s = serializers.PublisherSerializer(publisher)
#         return Response(s.data)
#
#     # 修改出版社信息
#     def put(self, request, pk, format=None):
#         publisher = self.get_object(pk)
#         s = serializers.PublisherSerializer(publisher, data=request.data)
#         if s.is_valid():
#             s.save()
#             return Response(s.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     # 删除出版社信息
#     def delete(self, request, pk, format=None):
#         publisher = self.get_object(pk)
#         publisher.delete()
#         return Response(status=status.HTTP_404_NOT_FOUND)


# 第二种
# class PublisherDetail(mixins.RetrieveModelMixin,
#                       mixins.UpdateModelMixin,
#                       mixins.DestroyModelMixin,
#                       generics.GenericAPIView):
#
#     queryset = models.Publisher.objects.all()
#     serializer_class = serializers.PublisherSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
#
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
#
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)


# 第三种

class PublisherDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = models.Publisher.objects.all()
    serializer_class = serializers.PublisherSerializer
    permission_classes = (IsOwnerOrReadOnly,)


class BookList(generics.ListCreateAPIView):
    queryset = models.Book.objects.all()
    serializer_class = serializers.BookSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Book.objects.all()
    serializer_class = serializers.BookSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'publishers': reverse('publisher-list', request=request, format=format),
        'book': reverse('book-list', request=request, format=format)
    })