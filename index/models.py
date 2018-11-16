from django.db import models
from django.contrib.auth.models import User
from xadmin.plugins import auth
from DjangoUeditor.models import UEditorField
from uprofile.models import Uprofile

# Create your models here.
# 新闻中心
class NewsCenter(models.Model):
    choices = (
        (False, '保存'),
        (True, '删除'),
    )
    news_title = models.CharField(max_length=50, verbose_name='新闻标题', null=False)
    news_time = models.DateTimeField(verbose_name='新闻时间', null=False)
    content = UEditorField(verbose_name='新闻内容',width=600,height=300, toolbars="full", imagePath="media/news/", filePath="media/news/", upload_settings={"imageMaxSize":1204000},default='')
    create_at = models.DateTimeField(auto_now_add=True, editable=False, verbose_name='编辑时间', null=False)
    update_at = models.DateTimeField(auto_now_add=True, editable=False, verbose_name='更新时间', null=False)
    create_by = models.ForeignKey(Uprofile, verbose_name='编辑人', null=False, on_delete=False)# 编辑人 editable=False default =当前登录的id, editable=False, default=User
    is_delete = models.BooleanField(choices=choices, default=False, null=False, verbose_name='逻辑删除', db_index=True)

    class Meta:
        db_table = 'NewsCenter'
        ordering = ('create_at', )
        verbose_name = '新闻中心'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.news_title
