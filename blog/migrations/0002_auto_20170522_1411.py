# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-date'], 'verbose_name': '\u6587\u7ae0', 'verbose_name_plural': '\u6587\u7ae0'},
        ),
        migrations.AlterModelOptions(
            name='link',
            options={'ordering': ['-sitename'], 'verbose_name': '\u53cb\u60c5\u94fe\u63a5', 'verbose_name_plural': '\u53cb\u60c5\u94fe\u63a5'},
        ),
        migrations.AlterField(
            model_name='article',
            name='date',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x8f\x91\xe5\xb8\x83\xe6\x97\xa5\xe6\x9c\x9f'),
        ),
        migrations.AlterField(
            model_name='user',
            name='photo',
            field=models.ImageField(default=b'default.png', upload_to=b'%Y/%m', max_length=200, verbose_name=b'\xe5\xa4\xb4\xe5\x83\x8f'),
        ),
    ]
