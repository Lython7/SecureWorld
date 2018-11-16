from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.
class Uprofile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='用户')
    uname = models.CharField(max_length=32, null=True, verbose_name='用户姓名')
    ucellphone = models.CharField(max_length=11, null=False, verbose_name='手机号码', unique=True)
    uposition = models.CharField(max_length=20, null=False, verbose_name='岗位名称')

    class Meta:
        db_table = 'uprofile'
        verbose_name = '用户信息拓展表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.uname

    def __unicode__(self):
        return self.uname

    # 重写save方法，最后判断完成后，调用父类save方法。
    def save(self, *args, **kwargs):
        if not self.pk:
            try:
                profile = Uprofile.objects.get(user=self.user)
                self.pk = profile.pk
            except Uprofile.DoesNotExist:
                pass
        super(Uprofile, self).save(*args, **kwargs)


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        profile = Uprofile()
        profile.user = instance

        if profile.user_id == 1:
            profile.uname = '超级管理员'
            profile.ucellphone = '18999999999'
            profile.uposition = '运维工程师'
            profile.save()
        else:
            profile.save()
            # 此处需要根据权限 save配置权限表格

post_save.connect(create_user_profile, sender=User)

