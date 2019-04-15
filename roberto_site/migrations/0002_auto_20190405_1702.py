# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-04-05 16:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roberto_site', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='portraits',
            name='image',
        ),
        migrations.AddField(
            model_name='portraits',
            name='image1',
            field=models.ImageField(default='wef', upload_to='images/portraits<django.db.models.fields.CharField>'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='portraits',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to='images/portraits<django.db.models.fields.CharField>'),
        ),
        migrations.AddField(
            model_name='portraits',
            name='image3',
            field=models.ImageField(blank=True, null=True, upload_to='images/portraits<django.db.models.fields.CharField>'),
        ),
        migrations.AddField(
            model_name='portraits',
            name='image4',
            field=models.ImageField(blank=True, null=True, upload_to='images/portraits<django.db.models.fields.CharField>'),
        ),
        migrations.AddField(
            model_name='portraits',
            name='image5',
            field=models.ImageField(blank=True, null=True, upload_to='images/portraits<django.db.models.fields.CharField>'),
        ),
    ]