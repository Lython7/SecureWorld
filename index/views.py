from django.forms import model_to_dict
from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from .models import *

# Create your views here.

def index(request):
    return render_to_response('index/index.html', context={'PageTitle':'万铎科技'}, status=200)

def newsCenter(request):
    news = NewsCenter.objects.filter(is_delete=False).values_list()
    return render_to_response('index/newsCenter.html', context={'PageTitle':'新闻中心-万铎科技', 'news': news}, status=200)

def newsDetail(request, news_id):
    try:
        news = model_to_dict(NewsCenter.objects.filter(is_delete=False).get(id=int(news_id)))
        return render_to_response('index/newsDetail.html', context={'PageTitle': '新闻资讯-万铎科技',
                                                                    'title': news['news_title'],
                                                                    'time': news['news_time'],
                                                                    'content': news['content'],}, status=200)
    except:
        return HttpResponse('miss it!')


def product(request):
    return render_to_response('index/product.html', context={'PageTitle': '产品简介-万铎科技'}, status=200)

def service(request):
    return render_to_response('index/service.html', context={'PageTitle': '服务-万铎科技'}, status=200)

def contact(request):
    return render_to_response('index/contact.html', context={'PageTitle': '联系我们-万铎科技'}, status=200)