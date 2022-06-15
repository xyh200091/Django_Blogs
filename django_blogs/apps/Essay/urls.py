from django.urls import path
from . import views

urlpatterns = [
    path(r'classify/get/', views.GetClassifyView.as_view()),  # 查询分类
    path(r'classify/del/', views.DelClassifyView.as_view()),  # 删除分类
    path(r'classify/add/', views.AddClassifyView.as_view()),  # 添加分类
    path(r'label/get/', views.GetLabelView.as_view()),  # 查询分类
    path(r'label/del/', views.DelLabelView.as_view()),  # 删除分类
    path(r'label/add/', views.AddLabelView.as_view()),  # 添加分类
]