from django.utils.deprecation import MiddlewareMixin
import uuid
from django_redis import get_redis_connection

from django_blogs.lib.Encode import *

from django_blogs.data.Time import *


# 绑定id
class BoundId(MiddlewareMixin):
    def process_response(self, request, response):
        """
        1、获取cookies
        2、验证cookies
        3、生成id
        4、保存id
        5、返回cookie
        6、重置cookie保存时间
        """
        userNum = request.COOKIES.get('userNum')
        user_bank = get_redis_connection('user')
        if userNum is None:
            user_uuid = MD5(str(uuid.uuid1()))
            user_bank.set('user_'+user_uuid,user_uuid,REDIS_USER_ID_TIME)
            response.set_cookie('userNum',user_uuid,max_age=REDIS_USER_ID_TIME)
        else:
            if user_bank.get('user_'+userNum):
                user_bank.set('user_' + userNum, userNum, REDIS_USER_ID_TIME)
                response.set_cookie('userNum', userNum, max_age=REDIS_USER_ID_TIME)

        return response
