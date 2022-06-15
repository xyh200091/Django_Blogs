from django.urls import path
from . import views

urlpatterns = [
    path(r'classify/get/', views.GetClassifyView.as_view()),
    path(r'classify/del/', views.DelClassifyView.as_view()),
]
