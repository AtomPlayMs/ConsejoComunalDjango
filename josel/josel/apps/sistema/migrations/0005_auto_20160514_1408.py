# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-14 18:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0004_publicacion_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicacion',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='Publicaciones'),
        ),
    ]
