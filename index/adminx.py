#coding:utf-8
import xadmin
from index.models import NewsCenter
from xadmin import views


class BaseSetting(object):
    # 主题修改
    enable_themes = True
    use_bootswatch = True


class GlobalSetting(object):
    site_title = '万铎科技后台管理'
    site_footer = '北京万铎科技服务有线公司'
    # menu_style = "accordion"

class NewsCenter_Admin(object):
    list_display = ('news_title', 'news_time', 'create_at', 'create_by', )
    search_fields = ('news_title', 'news_time', 'create_at', 'create_by', )
    ordering = ('create_at',)
    list_per_page = 20
    style_fields = {"content": "ueditor"}

xadmin.site.register(NewsCenter, NewsCenter_Admin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSetting)

