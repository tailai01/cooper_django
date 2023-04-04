#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time          : 2022/12/3 17:38
# File          : urls.py
# @Author       : MingTai
from django.urls import path
from . import views

app_name = 'users'

# 子路由
urlpatterns = [
    # 注册子路由
    path('register/', views.RegisterView.as_view(), name='register'),
    path('username/<username>/count', views.UserNameCountView.as_view(), name='count'),
]
