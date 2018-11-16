from django.db import models
from xadmin.plugins import auth

from DjangoUeditor.models import UEditorField

# Create your models here.
# 新闻中心
class NewsCenter(models.Model):
    choices = (
        (False, '保存'),
        (True, '删除'),
    )
    # choices_area = (
    #     (1,'重磅新闻，页面最上'),
    #     (2,'次要新闻，页面中间'),
    #     (3,'其他新闻'),
    # )
    news_title = models.CharField(max_length=50, verbose_name='新闻标题', null=False)
    # display_area = models.IntegerField(choices=choices_area, default=2)
    news_time = models.DateTimeField(verbose_name='新闻时间', null=False)
    content = UEditorField(verbose_name='新闻内容',width=800,height=1200,imagePath='',filePath='',)
    create_at = models.DateTimeField(auto_now_add=True, editable=False, verbose_name='编辑时间', null=False)
    update_at = models.DateTimeField(auto_now_add=True, editable=False, verbose_name='更新时间', null=False)
    create_by = models.ForeignKey('auth.User', verbose_name='编辑人', null=False, on_delete=False, editable=False)# 编辑人 editable=False default =当前登录的id, editable=False, default=User
    is_delete = models.BooleanField(choices=choices, default=False, null=False, verbose_name='逻辑删除', db_index=True)

    class Meta:
        db_table = 'NewsCenter'
        ordering = ('create_at', )
        verbose_name = '新闻中心'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.news_title