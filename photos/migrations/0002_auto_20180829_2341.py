# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-29 23:41
from __future__ import unicode_literals

from django.db import migrations, models
import photos.models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='file',
            field=models.ImageField(upload_to=photos.models.upload),
        ),
    ]