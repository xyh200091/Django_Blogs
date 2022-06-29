from django.shortcuts import render
from django.views import View
from django_redis import get_redis_connection
from django import http

import time
import re
import json
import math

from django_blogs.data.Time import *
from django_blogs.data.EssayCode import *

from User.models import OwnerMessage


# 登录后端
class LoginAdminView(View):
    def post(self, request):
        """
        1、接受参数
        2、验证数据
            格式验证
            数据验证
        3、添加session
        4、返回信息
        """
        message = {
            'code': CORRECT,
            'info': ''
        }
        data = json.loads(request.body)
        try:
            username = data['username']  # 用户名
            password = data['password']  # 密码
            img_code = data['img_code']  # 验证码
            t = data['time']  # 请求时间戳
        except KeyError:
            return http.JsonResponse({
                'code': USER_ACCOUNT,
                'info': '数据缺失'
            })
        userNum = request.COOKIES.get('userNum')
        code_bank = get_redis_connection('code')
        if not re.match(r'^[0-9a-zA-Z]{4}$', img_code) or code_bank.get(
                "img_code_" + userNum).decode().lower() != img_code.lower():
            return http.JsonResponse({
                'code': USER_IMG_CODE,
                'info': '验证码错误'
            })

        if (not re.match(r'^[a-zA-Z][a-zA-Z0-9]{4,19}$', username)):
            return http.JsonResponse({
                'code': USER_ACCOUNT,
                'info': '用户名或密码不正确'
            })
        try:
            user_data = OwnerMessage.objects.get(username=username)
        except OwnerMessage.DoesNotExist:
            return http.JsonResponse({
                'code': USER_ACCOUNT,
                'info': '用户名或密码不正确'
            })
        else:
            if user_data.password != password:
                return http.JsonResponse({
                    'code': USER_ACCOUNT,
                    'info': '用户名或密码不正确'
                })
            else:
                # 设置状态保持和时间限制
                request.session[userNum] = username
                request.session.set_expiry(USER_STATE_TIME)

                return http.JsonResponse({
                    'code': CORRECT,
                    'info': "登录成功"
                })


# 登录验证
class VerifyLoginView(View):
    def get(self, request):
        """
        1、获取userNum
        2、获取session
        3、验证数据
        4、返回信息
        """
        userNum = request.COOKIES.get('userNum')
        session = request.session.get(userNum)

        if session:
            return http.JsonResponse({
                'code': CORRECT
            })
        else:
            return http.JsonResponse({
                'code': USER_VERIFY
            })


class LoginOutView(View):
    def get(self, request):
        """
        1、获取数据
        2、验证数据
        3、清除数据
        4、返回状态
        """
        t = request.GET.get('time')
        userNum = request.COOKIES.get('userNum')
        if math.fabs(time.time() - int(t)) > 60:
            return http.JsonResponse({
                'code': TIME_EXCEED,
                'info': "超时连接"
            })

        if not request.session.get(userNum):
            return http.JsonResponse({
                'code': USER_NOT,
                'info': "未登录"
            })

        del request.session[userNum]
        response = http.JsonResponse({
            'code': CORRECT,
            'info': "成功"
        })
        response.delete_cookie('sessionid')

        return response


