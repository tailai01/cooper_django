from django.db import models

# Create your models here.

# from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser


# 使用系统自带的user信息，继承AbstractUser 并重写
class User(AbstractUser):
    mobile = models.CharField(max_length=11, unique=True)

    class Meta:
        db_table = 'tb_users'
        verbose_name = '用户管理表'
        verbose_name_plural = verbose_name
