# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-14 17:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0003_auto_20160514_1020'),
    ]

    operations = [
        migrations.AddField(
            model_name='publicacion',
            name='thumbnail',
            field=models.ImageField(blank=True, max_length=500, null=True, upload_to='Publicaciones'),
        ),
    ]