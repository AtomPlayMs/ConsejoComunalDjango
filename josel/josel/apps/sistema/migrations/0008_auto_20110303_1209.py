# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2011-03-03 16:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0007_auto_20110303_0331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicacion',
            name='fecha',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Fecha'),
        ),
    ]