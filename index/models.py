# coding: utf-8
import os
from datetime import datetime
from django.db import models
from django.contrib.auth.models import User

from SecureWorld.settings import MEDIA_ROOT
from xadmin.plugins import auth
from DjangoUeditor.models import UEditorField
from uprofile.models import Uprofile

def makePath():
    timeList = datetime.now().strftime("%Y-%m-%d").split('-')
    tPath = os.path.join('news', timeList[0], timeList[1], timeList[2])
    fPath = os.path.join(MEDIA_ROOT, tPath)
    isExists=os.path.exists(fPath)
    if not isExists:
        os.makedirs(fPath)
        # print('创建目录：' + fPath)

def delete_gap_dir(path):
    if os.path.isdir(path):
        for d in os.listdir(path):
            delete_gap_dir(os.path.join(path, d))
        if not os.listdir(path):
            os.rmdir(path)
            # print('移除空目录: ' + path)

def NewsTitlePicPath(instance, filename):
    timeList = datetime.now().strftime("%Y-%m-%d").split('-')
    return "{0}/{1}/{2}/{3}/{4}".format('news', timeList[0], timeList[1], timeList[2], filename)

# 新闻中心
class NewsCenter(models.Model):
    def __init__(self, *args, **kwargs):
        models.Model.__init__(self, *args, **kwargs)
        delete_gap_dir(os.path.join(MEDIA_ROOT, 'news'))
        makePath()

    choices = ((False, '保存'), (True, '删除'),)
    level_choices = ((2,'重磅新闻'), (1,'列表新闻'),)

    title = models.CharField(max_length=50, verbose_name='新闻标题', null=False)
    image = models.ImageField(verbose_name='新闻图片-展示', null=False, upload_to=NewsTitlePicPath)
    news_time = models.DateTimeField(verbose_name='新闻时间', null=False, default=datetime.now)
    level = models.SmallIntegerField(verbose_name='新闻级别', null=False, default=1, choices=level_choices, db_index=True)
    content = UEditorField(verbose_name='新闻内容',width=1000,height=600, toolbars="full", upload_settings={"imageMaxSize":1204000},default='')
    is_delete = models.BooleanField(choices=choices, default=False, null=False, verbose_name='逻辑删除', db_index=True)

    create_time = models.DateTimeField(auto_now_add=True, editable=False, verbose_name='编辑时间', null=False)
    update_time = models.DateTimeField(auto_now=True, editable=False, verbose_name='更新时间', null=False)
    create_by = models.ForeignKey(Uprofile, verbose_name='编辑人', on_delete=models.SET_NULL, null=True, editable=False)# 编辑人 editable=False default =当前登录的id, editable=False, default=User

    class Meta:
        db_table = 'NewsCenter'
        ordering = ('create_time', )
        verbose_name = '新闻中心'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title

    # def __del__(self):
    #     print('删除')
