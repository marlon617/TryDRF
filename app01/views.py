from django.shortcuts import render
from django.http import HttpResponse


from app01 import models


def publisher_list(request):

    queryset = models.Publisher.objects.all()

    #1.序列化
    # data = []
    # for i in queryset:
    #     p_tmp = {
    #         "name": i.name,
    #         "address": i.address
    #     }
    #
    #     data.append(p_tmp)
    # import json
    # return HttpResponse(json.dumps(data), content_type="application/json")

    # 2.
    # data = []
    # from django.forms.models import model_to_dict
    # for i in queryset:
    #     data.append(model_to_dict(i))

    # import json
    # return HttpResponse(json.dumps(data), content_type="application/json")

    # 3.

    # from django.core import serializers
    # data = serializers.serialize("json", queryset)
    #
    # return HttpResponse(data, content_type="application/json")



    from app01 import serializers

    serializer = serializers.PublisherSerializer(queryset, many=True)
    import json
    return HttpResponse(json.dumps(serializer.data), content_type="application/json")