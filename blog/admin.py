# -*- coding: utf-8 -*-
from django.contrib import admin
from models import *

# Register your models here.

class ArticleAdmin(admin.ModelAdmin):

	class Media:
		js = (
			'/static/js/kindeditor-4.1.10/kindeditor-min.js',
			'/static/js/kindeditor-4.1.10/lang/zh_CN.js',
			'/static/js/kindeditor-4.1.10/config.js',
		)

admin.site.register(User)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Sort)
admin.site.register(Link)

