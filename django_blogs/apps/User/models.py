from django.db import models


# Create your models here.

# 管理员信息数据库
class OwnerMessage(models.Model):
    username = models.CharField(max_length=30, unique=True, primary_key=True)  # 用户名
    password = models.CharField(max_length=999, null=True)  # 密码
    name = models.CharField(max_length=20, unique=True, null=True)  # 管理员名称
