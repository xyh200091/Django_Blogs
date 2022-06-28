from django.urls import path
from . import views

urlpatterns = [
    path('login/admin', views.LoginAdminView.as_view()),  # 登录后端
    path('login/verify', views.VerifyLoginView.as_view()),  # 验证登录
]
