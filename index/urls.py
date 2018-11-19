from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^index/$', views.index),
    url(r'^index/newsCenter/$', views.newsCenter, name='newsCenter'),
    url(r'^index/newsDetail/(\d*)', views.newsDetail, name='newsDetail'),
    url(r'^index/product/$', views.product, name='product'),
    url(r'^index/service/$', views.service, name='service'),
    url(r'^index/contact/$', views.contact, name='contact'),
    ]