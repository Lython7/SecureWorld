import xadmin
from .models import *

# 后台django管理名字修改

class NewsCenter_Admin(xadmin.AdminSite):
    list_display = ('news_title', 'news_time', 'create_at', 'create_by', )
    search_fields = ('news_title', 'news_time', 'create_at', 'create_by', )
    ordering = ('create_at',)
    list_per_page = 20

xadmin.site.register(NewsCenter, NewsCenter_Admin)
