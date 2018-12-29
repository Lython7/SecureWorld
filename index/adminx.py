#coding:utf-8
import xadmin
from index.models import NewsCenter
from xadmin import views
from xadmin.sites import register


class BaseXadminSetting(object):
    # 主题修改
    enable_themes = True
    use_bootswatch = True


class GlobalXadminSetting(object):
    site_title = '万铎科技后台管理'
    site_footer = '北京万铎科技服务有线公司'
    menu_style = "accordion"

class NewsCenterXadmin(object):
    list_display = ('title', 'news_time', 'create_time', 'create_by', )
    search_fields = ('title', 'news_time', 'create_time', 'create_by', )
    # list_filter = ('',)
    ordering = ('create_time',)
    list_per_page = 20
    style_fields = {"content": "ueditor"}
    # readonly_fields = ('create_by',)
    model_icon = "fa fa-file-text"

    def save_models(self):
        self.new_obj.create_by = self.request.user
        super().save_models()

xadmin.site.register(NewsCenter, NewsCenterXadmin)
xadmin.site.register(views.BaseAdminView, BaseXadminSetting)
xadmin.site.register(views.CommAdminView, GlobalXadminSetting)

