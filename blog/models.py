# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
# user
# 采用的继承方式扩展用户信息
class User(AbstractUser):
	nickname = models.CharField(max_length=60, verbose_name='昵称')
	photo = models.ImageField(upload_to='%Y/%m', default='default.png', max_length=200, verbose_name='头像')

	class Meta:
		verbose_name = '用户'
		verbose_name_plural = verbose_name
		ordering = ['-id']

	def __unicode__(self):
		return self.username

# sort
class Sort(models.Model):
	sortname = models.CharField(max_length=255, verbose_name='分类')

	class Meta:
		verbose_name = '分类'
		verbose_name_plural = verbose_name
		ordering = ['id']

	def __unicode__(self):
		return self.sortname

# article
class Article(models.Model):
	title = models.CharField(max_length=255, verbose_name='文章标题')
	date = models.DateTimeField(auto_now_add=True, verbose_name='发布日期')
	content = models.TextField(verbose_name='文章内容')
	author = models.ForeignKey(User, verbose_name='用户')
	sortid = models.ForeignKey(Sort,blank=True, null=True, verbose_name='分类')

	class Meta:
		verbose_name = '文章'
		verbose_name_plural = verbose_name
		ordering = ['-date']

	def __unicode__(self):
		return self.title

# options
class Option(models.Model):
	option_name = models.CharField(max_length=255, verbose_name='设置名称')
	option_value = models.CharField(max_length=8000, verbose_name='设置内容')

	class Meta:
		verbose_name = '设置名称'
		verbose_name_plural = verbose_name

	def __unicode__(self):
		return self.option_name

# friend links
class Link(models.Model):
	sitename = models.CharField(max_length=30, verbose_name='站点名称')
	siteurl = models.CharField(max_length=75, verbose_name='站点地址')
	hide = models.BooleanField(default=True, verbose_name='是否显示')

	class Meta:
		verbose_name = '友情链接'
		verbose_name_plural = verbose_name
		ordering = ['-sitename']

	def __unicode__(self):
		return self.sitename