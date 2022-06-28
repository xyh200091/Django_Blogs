from django.shortcuts import render
from django.views import View
from django_redis import get_redis_connection
from django import http

import os
import time
import re
import json
import math

from django_blogs.lib.ImgCode import image_code
from django_blogs.data.Time import *
from django_blogs.data.EssayCode import *


# Create your views here.


# 获取验证码图片
class GetLoginCodeImgView(View):
    def get(self, request):
        """
        (
            1、获取请求时间戳
            2、获取当前时间戳
            3、比较时间戳
        )
        1、获取cookie
        2、验证cookie
        3、生成图片
        4、保存验证码
        5、返回验证码图片
        """
        t = int(request.GET.get('time'))
        T = time.time()
        if math.fabs(T - t) > 60:
            with open('lose.jpeg', 'rb') as f:
                image = f.read()
        else:
            userNum = request.COOKIES.get('userNum')
            img, text = image_code()
            code_bank = get_redis_connection('code')
            code_bank.set('img_code_' + userNum, text, REDIS_USER_LOGIN_TIME)

            img.save(userNum + ".jpg")
            with open(userNum + '.jpg', 'rb') as f:
                image = f.read()

            os.remove(userNum + '.jpg')

        response = http.HttpResponse(image, content_type='image/jpeg')
        response['Content-Disposition'] = 'attachment; filename="piece.jpeg"'
        return response



