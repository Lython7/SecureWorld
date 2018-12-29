# import xadmin
# from xadmin.views import BaseAdminPlugin, CreateAdminView, ModelFormAdminView, UpdateAdminView
# from DjangoUeditor.models import UEditorField
# from DjangoUeditor.widgets import UEditorWidget
# from django.conf import settings
#
#
# class XadminUEditorWidget(UEditorWidget):
#     def __init__(self,**kwargs):
#         self.ueditor_options=kwargs
#         self.Media.js = None
#         super(XadminUEditorWidget,self).__init__(kwargs)
#
#
# class UeditorPlugin(BaseAdminPlugin):
#
#     def get_field_style(self, attrs, db_field, style, **kwargs):
#         if style == 'ueditor':
#             if isinstance(db_field, UEditorField):
#                 widget = db_field.formfield().widget
#                 param = {}
#                 param.update(widget.ueditor_settings)
#                 param.update(widget.attrs)
#                 return {'widget': XadminUEditorWidget(**param)}
#         return attrs
#
#     def block_extrahead(self, context, nodes):
#         js = '<script type="text/javascript" src="%s"></script>' % (settings.STATIC_URL + "ueditor/ueditor.config.js")         #自己的静态目录
#         js += '<script type="text/javascript" src="%s"></script>' % (settings.STATIC_URL + "ueditor/ueditor.all.min.js")   #自己的静态目录
#         nodes.append(js)
#
# xadmin.site.register_plugin(UeditorPlugin, UpdateAdminView)
# xadmin.site.register_plugin(UeditorPlugin, CreateAdminView)


# -*- coding: utf-8 -*-
from django.db.models import TextField

import xadmin
from xadmin.views import BaseAdminPlugin, CreateAdminView,UpdateAdminView
from DjangoUeditor.models import UEditorField
from DjangoUeditor.widgets import UEditorWidget
from django.conf import settings
class XadminUEditorWidget(UEditorWidget):
    def __init__(self,**kwargs):
        self.ueditor_options=kwargs
        self.Media.js = None
        super(XadminUEditorWidget,self).__init__(kwargs)
class UeditorPlugin(BaseAdminPlugin):
    def get_field_style(self, attrs, db_field, style, **kwargs):
        if style == 'ueditor':
            if isinstance(db_field, UEditorField):
                widget = db_field.formfield().widget
                param = {}
                param.update(widget.ueditor_settings)
                param.update(widget.attrs)
                return {'widget': XadminUEditorWidget(**param)}
            if isinstance(db_field, TextField):
                return {'widget': XadminUEditorWidget}
        return attrs
    # Media,添加到footer中的js文件
    def get_media(self, media):
        media = media + self.vendor('xadmin.widget.select.js','xadmin.widget.select-transfer.js','xadmin.plugin.quick-form.js')
        return media
    #添加到header中的css和js文件
    def block_extrahead(self, context, nodes):
        js ='<link href="/static/xadmin/vendor/select2/select2.css" type="text/css" media="screen" rel="stylesheet" />'
        js +='<link href="/static/xadmin/vendor/selectize/selectize.css" type="text/css" media="screen" rel="stylesheet" />'
        js +='<link href="/static/xadmin/vendor/selectize/selectize.bootstrap3.css" type="text/css" media="screen" rel="stylesheet" />'
        js +='<link href="/static/xadmin/css/xadmin.widget.select-transfer.css" type="text/css" media="screen" rel="stylesheet" />'

        js +='<link href="/static/xadmin/vendor/bootstrap-clockpicker/bootstrap-clockpicker.css" type="text/css" media="screen" rel="stylesheet" />'
        js +='<link href="/static/xadmin/vendor/bootstrap-datepicker/css/datepicker.css"  type="text/css" media="screen" rel="stylesheet" />'
        js +='<link href=""  type="text/css" media="screen" rel="stylesheet" />'
        js +='<link href=""  type="text/css" media="screen" rel="stylesheet" />'




        js +='<script type="text/javascript" src="/static/xadmin/vendor/selectize/selectize.js"></script>'
        js +='<script type="text/javascript" src="/static/xadmin/vendor/select2/select2.js"></script>'
        js +='<script type="text/javascript" src="/static/xadmin/vendor/select2/select2_locale_zh-hans.js"></script>'

        js +='<script type="text/javascript" src="/static/xadmin/vendor/bootstrap-clockpicker/bootstrap-clockpicker.js"></script>'
        js +='<script type="text/javascript" src="/static/xadmin/vendor/bootstrap-datepicker/js/bootstrap-datepicker.js"></script>'
        js +='<script type="text/javascript" src="/static/xadmin/js/xadmin.widget.datetime.js"></script>'
        js +='<script type="text/javascript" src=""></script>'
        js +='<script type="text/javascript" src=""></script>'



        #js +='<script type="text/javascript" src="/static/xadmin/js/xadmin.widget.select.js"></script>'
        #js +='<script type="text/javascript" src="/static/xadmin/js/xadmin.widget.select-transfer.js"></script>'
        #js +='<script type="text/javascript" src="/static/xadmin/js/xadmin.plugin.quick-form.js"></script>'
        js += '<script type="text/javascript" src="%s"></script>' % (settings.STATIC_URL + "ueditor/ueditor.config.js")
        js += '<script type="text/javascript" src="%s"></script>' % (settings.STATIC_URL + "ueditor/ueditor.all.min.js")
        nodes.append(js)
xadmin.site.register_plugin(UeditorPlugin, UpdateAdminView)
xadmin.site.register_plugin(UeditorPlugin, CreateAdminView)