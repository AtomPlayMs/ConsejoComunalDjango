# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-14 14:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicacion',
            name='url_album',
            field=models.CharField(max_length=600, verbose_name='Link de album en facebook'),
        ),
    ]