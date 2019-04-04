# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-04-04 21:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roberto_site', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='families',
            name='description',
            field=models.TextField(default='1'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='food',
            name='description',
            field=models.TextField(default='123'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='music',
            name='description',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='portraits',
            name='description',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='weddings',
            name='description',
            field=models.TextField(default='erghaer'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='families',
            name='image',
            field=models.ImageField(upload_to='images/families'),
        ),
        migrations.AlterField(
            model_name='food',
            name='image',
            field=models.ImageField(upload_to='images/food'),
        ),
        migrations.AlterField(
            model_name='music',
            name='image',
            field=models.ImageField(upload_to='images/music'),
        ),
        migrations.AlterField(
            model_name='weddings',
            name='image',
            field=models.ImageField(upload_to='images/weddings'),
        ),
    ]
