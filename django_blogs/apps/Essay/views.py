import json

import django.db.utils
from django.shortcuts import render
from django.views import View
from django import http

from Essay.models import ClassifyModel, LabelModel

from django_blogs.data.EssayCode import *


# 获取分类
class GetClassifyView(View):
    def get(self, request):
        Classifys = ClassifyModel.objects.all().values()
        Classify_list = []
        if Classifys:
            for Classify in Classifys:
                Classify_list.append(Classify)

            return http.JsonResponse({
                'code': CORRECT,
                'data': Classify_list
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

        try:
            Classify_Id = ClassifyModel.objects.get(Classify_Id=classify_Id)  # 查询数据
        except ClassifyModel.DoesNotExist:
            return http.JsonResponse({
                'code': SQL_LOSE,
                'info': "数据库操作失败"
            })
        else:
            Classify_Id.delete()

        return http.JsonResponse({
            'code': CORRECT,
            "info": "数据删除成功"
        })


# 添加分类
class AddClassifyView(View):
    def post(self, request):
        """
        1、验证登录
        2、获取数据
        3、保存数据
        4、返回运行结果
        """

        add_name = json.loads(request.body)['add_name']
        if add_name:
            try:
                ClassifyModel.objects.create(Classify_Name=add_name).save()
            except django.db.utils.IntegrityError:
                return http.JsonResponse({
                    'code': SQL_REDO,
                    "info": "数据重复"
                })
            else:
                return http.JsonResponse({
                    'code': CORRECT,
                    "info": "数据已写入"
                })
        else:
            return http.JsonResponse({
                'code': DATA_NULL,
                "info": "请求书记为空"
            })


# 获取标签
class GetLabelView(View):
    def get(self, request):
        Labels = LabelModel.objects.all().values()
        Label_list = []
        if Labels:
            for name in Labels:
                Label_list.append(name)

            return http.JsonResponse({
                'code': CORRECT,
                'data': Label_list
            })
        else:
            return http.JsonResponse({
                'code': DATA_NULL
            })


# 删除标签
class DelLabelView(View):
    def post(self, request):
        label_Id = json.loads(request.body)['label_Id']

        try:
            Label_Id = LabelModel.objects.get(Label_Id=label_Id)  # 查询数据
        except LabelModel.DoesNotExist:
            return http.JsonResponse({
                'code': SQL_LOSE,
                'info': "数据库操作失败"
            })
        else:
            Label_Id.delete()

        return http.JsonResponse({
            'code': CORRECT,
            "info": "数据删除成功"
        })


# 添加分类
class AddLabelView(View):
    def post(self, request):
        add_name = json.loads(request.body)['add_name']
        add_color = json.loads(request.body)['add_color']
        if add_name:
            try:
                LabelModel.objects.create(Label_Name=add_name, Label_Color=add_color).save()
            except django.db.utils.IntegrityError:
                return http.JsonResponse({
                    'code': SQL_REDO,
                    "info": "数据重复"
                })
            else:
                return http.JsonResponse({
                    'code': CORRECT,
                    "info": "数据已写入"
                })
        else:
            return http.JsonResponse({
                'code': DATA_NULL,
                "info": "请求书记为空"
            })