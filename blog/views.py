# -*- coding: utf-8 -*-
import logging
from django.shortcuts import render
from django.conf import settings
from django.core.paginator import Paginator, InvalidPage, EmptyPage, PageNotAnInteger
from django.http import HttpResponse,HttpResponseRedirect
from models import *

logger = logging.getLogger('blog.views')

# Create your views here.
def global_setting(request):
	return {'SITE_NAME': settings.SITE_NAME}

def index(request):
	try:
		# 分类信息获取 （导航数据）
		sort_list = Sort.objects.all()
		# 友情链接数据
		friend_link = Link.objects.all()
		# 最新文章数据
		article_content = Article.objects.all()
		paginator = Paginator(article_content, 10)
		try:
			page = int(request.GET.get('page', 1))
			article_content = paginator.page(page)
		except (EmptyPage, InvalidPage, PageNotAnInteger):
			article_content = paginator.page(1)

	except Exception as e:
		logger.error(e)
	return render(request, 'index.html', locals())

def detail(request,aid):
	try:
		sort_list = Sort.objects.all()
		friend_link = Link.objects.all()
		post = Article.objects.all()
		if post[int(aid)-1]:
			return render(request, 'article.html',{'sort_list': sort_list, 'friend_link': friend_link,'post':post[int(aid)-1], 'aid': aid})

	except Exception as e:
		logger.error(e)
	return HttpResponseRedirect('/')

def sortdetail(request,sid):
	sort_list = Sort.objects.all()
	friend_link = Link.objects.all()
	articles = Article.objects.all()
	try:
		ssid = int(sid)
		if sort_list[ssid-2]:
			return render(request, 'sortdetail.html',{'sort_list': sort_list, 'friend_link': friend_link, 'articles': articles, 'ssid': ssid})
	except Exception as e:
		logger.error(e)
	return HttpResponseRedirect('/')
