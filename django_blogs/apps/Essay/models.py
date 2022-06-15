from django.db import models


# Create your models here.
# 分类数据库
class Classify(models.Model):
    Classify_Id = models.AutoField(primary_key=True)  # 分类ID
    Classify_Name = models.CharField(max_length=50,blank=False,unique=True)