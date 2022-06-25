from django.utils.deprecation import MiddlewareMixin
import uuid
from django_redis import get_redis_connection


# 绑定id
class BoundId(MiddlewareMixin):
    def process_response(self, request, response):
        """
        1、获取cookies
        2、验证cookies
        3、生成id
        4、保存id
        5、返回cookie
        """
        userNum = request.COOKIES.get('userNum')
        if userNum is None:
            user_uuid = uuid.uuid1()

            user_bank = get_redis_connection('user')
        return response
