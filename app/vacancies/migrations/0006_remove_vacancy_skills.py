# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-30 14:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vacancies', '0005_auto_20170830_1454'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vacancy',
            name='skills',
        ),
    ]
