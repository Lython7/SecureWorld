from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User


# Create your models here.
class Uprofile(AbstractUser):
    id = models.AutoField(primary_key=True)
    nick_name = models.CharField(max_length=32, null=True, blank=True, verbose_name='用户昵称', default='丑八怪')
    birthday = models.DateTimeField(verbose_name='出生日期', default='1900-01-01')
    ucellphone = models.CharField(max_length=11, null=True, verbose_name='手机号码', unique=True)
    uposition = models.CharField(max_length=30, default='', verbose_name='工作岗位')

    class Meta:
        verbose_name = '用户信息表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username

    def __unicode__(self):
        return self.username

# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         profile = Uprofile()
#
#         if profile.user_id == 1:
#             profile.uname = 'admin'
#             profile.ucellphone = '18999999999'
#             profile.upower = 100
#             profile.ustatus = 1
#             profile.save()
#         else:
#             profile.save()
#             # 此处需要根据权限 save配置权限表格
#
# post_save.connect(create_user_profile, sender=User)


