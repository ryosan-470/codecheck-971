# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-13 07:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='created_at',
            field=models.DateTimeField(),
        ),
    ]