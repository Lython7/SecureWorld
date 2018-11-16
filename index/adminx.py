#coding:utf-8
import xadmin
from xadmin import views

class BaseSetting(object):
    # 主题修改
    enable_themes = True
    use_bootswatch = True

class GlobalSetting(object):
    # 设置base_site.html的Title
    site_title = '万铎科技后台管理'
    # 设置base_site.html的Footer
    # site_footer  = '%s'.format(str(datetime.datetime.now())[:10])
    site_footer = '北京万铎科技服务有线公司'

xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSetting)