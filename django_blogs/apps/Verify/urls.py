from django.urls import path
from . import views

urlpatterns = [
    path('get/login/code/img', views.GetLoginCodeImgView.as_view()),  # 获取验证码
]
