# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-10 14:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('components', '0004_auto_20181010_1834'),
    ]

    operations = [
        migrations.AlterField(
            model_name='component',
            name='image',
            field=models.ImageField(null=True, upload_to='media'),
        ),
    ]
