# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20170522_1411'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sort',
            options={'ordering': ['id'], 'verbose_name': '\u5206\u7c7b', 'verbose_name_plural': '\u5206\u7c7b'},
        ),
    ]
