import json
from django.shortcuts import render
from django.views import View
from django import http

from Essay.models import Classify

from django_blogs.data.EssayCode import *


# 获取分类
class GetClassifyView(View):
    def get(self, request):
        names = Classify.objects.all().values()
        name_list = []
        if names:
            for name in names:
                name_list.append(name)

            return http.JsonResponse({
                'code': CORRECT,
                'data': name_list
            })
        else:
            return http.JsonResponse({
                'code': DATA_NULL
            })


# 删除分类
class DelClassifyView(View):
    def post(self, request):
        """
        1、验证登录
        2、获取数据
        3、删除数据
        """
        classify_Id = json.loads(request.body)['classify_Id']

        Classify_Id = Classify.objects.get(Classify_Id=classify_Id)  # 查询数据
        Classify_Id.delete()

        return http.JsonResponse({
            'code': CORRECT,
            "info": "数据删除成功"
        })
