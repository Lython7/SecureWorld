# coding: utf-8
from django.core.paginator import Paginator
from django.forms import model_to_dict
from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from .models import *

# Create your views here.

def index(request):
    return render_to_response('index/index.html', context={'PageTitle':'万铎科技'}, status=200)

def newsCenter(request, pindex=1):
    newsList=NewsCenter.objects.filter(is_delete=False).order_by("-create_time")
    paginator = Paginator(newsList, 1) # 分页处理
    try:
        page = paginator.page(int(pindex))
    except:
        page = paginator.page(1)
    context={'PageTitle':'新闻中心-万铎科技', 'page':page}
    return render_to_response('news/newsCenter.html', context, status=200)

def newsShow(request, news_id):
    news=NewsCenter.objects.filter(is_delete=False).get(id=int(news_id))
    context={'PageTitle':news.title+'-万铎科技', 'content':news.content}
    return render(request, 'news/newsShow.html', context, status=200)

def newsDetail(request, news_id):
    try:
        news=NewsCenter.objects.filter(is_delete=False).get(id=int(news_id))
        context={'PageTitle':news.title+'-万铎科技', 'content':news.content}
        return render_to_response('news/newsDetail.html', context, status=200)
    except:
        return HttpResponse('miss it!')


def product(request):
    return render_to_response('index/product.html', context={'PageTitle': '产品简介-万铎科技'}, status=200)

def service(request):
    return render_to_response('index/service.html', context={'PageTitle': '服务-万铎科技'}, status=200)

def contact(request):
    return render_to_response('index/contact.html', context={'PageTitle': '联系我们-万铎科技'}, status=200)



