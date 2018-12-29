from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^index/$', views.index),
    url(r'^news/newsCenter/$', views.newsCenter, name='newsCenter'),
    url(r'^news/newsCenter/(\d+)/$', views.newsCenter),# 参数是多少页 page
    url(r'^news/newsShow/(\d*)', views.newsShow, name='newsShow'),# 参数是新闻ID
    # url(r'^index/newsDetail/(\d*)', views.newsDetail, name='newsDetail'),
    url(r'^index/product/$', views.product, name='product'),
    url(r'^index/service/$', views.service, name='service'),
    url(r'^index/contact/$', views.contact, name='contact'),
    ]