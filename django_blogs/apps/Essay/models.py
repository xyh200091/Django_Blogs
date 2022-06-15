from django.db import models


# Create your models here.
# 分类数据库
class ClassifyModel(models.Model):
    Classify_Id = models.AutoField(primary_key=True)  # 分类ID
    Classify_Name = models.CharField(max_length=50, blank=False, unique=True)  # 分类名称


# 标签库
class LabelModel(models.Model):
    Label_Id = models.AutoField(primary_key=True)  # 标签ID
    Label_Color = models.CharField(max_length=10, blank=False, unique=True)  # 标签颜色
    Label_Name = models.CharField(max_length=50, blank=False, unique=True)  # 标签名称