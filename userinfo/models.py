from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractUser

class UProfile(AbstractUser):
    nick_name=models.CharField(max_length=50, verbose_name='用户昵称', default='')
    birthday=models.DateTimeField(verbose_name='出生日期', null=True, blank=True)
    gender=models.CharField(max_length=6, choices=(('male','男'),('female','女')),default='female',verbose_name='性别')
    cellphone=models.CharField(max_length=11, null=True, verbose_name='手机号', unique=True)
    position = models.CharField(max_length=20, null=True, verbose_name='岗位名称')

class Meta:
    db_table = 'uprofile'
    verbose_name= '用户信息'
    verbose_name_plural=verbose_name

def __str__(self):
    return self.username
