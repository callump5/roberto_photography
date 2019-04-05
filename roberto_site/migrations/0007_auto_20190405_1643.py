# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-05 16:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roberto_site', '0006_auto_20190405_1639'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='families',
            name='description',
        ),
        migrations.RemoveField(
            model_name='families',
            name='image',
        ),
        migrations.RemoveField(
            model_name='food',
            name='description',
        ),
        migrations.RemoveField(
            model_name='food',
            name='image',
        ),
        migrations.RemoveField(
            model_name='music',
            name='description',
        ),
        migrations.RemoveField(
            model_name='music',
            name='image',
        ),
        migrations.RemoveField(
            model_name='weddings',
            name='description',
        ),
        migrations.RemoveField(
            model_name='weddings',
            name='image',
        ),
        migrations.AddField(
            model_name='families',
            name='desc1',
            field=models.TextField(default='1', verbose_name='Image 1 Description'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='families',
            name='desc2',
            field=models.TextField(blank=True, help_text='Only required if image 2 is uploaded', null=True, verbose_name='Image 2 Description'),
        ),
        migrations.AddField(
            model_name='families',
            name='desc3',
            field=models.TextField(blank=True, help_text='Only required if image 3 is uploaded', null=True, verbose_name='Image 3 Description'),
        ),
        migrations.AddField(
            model_name='families',
            name='desc4',
            field=models.TextField(blank=True, help_text='Only required if image 4 is uploaded', null=True, verbose_name='Image 4 Description'),
        ),
        migrations.AddField(
            model_name='families',
            name='desc5',
            field=models.TextField(blank=True, help_text='Only required if image 5 is uploaded', null=True, verbose_name='Image 5 Description'),
        ),
        migrations.AddField(
            model_name='families',
            name='image1',
            field=models.ImageField(default='1', upload_to='images/families', verbose_name='Image 1'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='families',
            name='image2',
            field=models.ImageField(blank=True, help_text='Optional', null=True, upload_to='images/families', verbose_name='Image 2'),
        ),
        migrations.AddField(
            model_name='families',
            name='image3',
            field=models.ImageField(blank=True, help_text='Optional', null=True, upload_to='images/families', verbose_name='Image 3 Description'),
        ),
        migrations.AddField(
            model_name='families',
            name='image4',
            field=models.ImageField(blank=True, help_text='Optional', null=True, upload_to='images/families', verbose_name='Image 4 Description'),
        ),
        migrations.AddField(
            model_name='families',
            name='image5',
            field=models.ImageField(blank=True, help_text='Optional', null=True, upload_to='images/families', verbose_name='Image 5 Description'),
        ),
        migrations.AddField(
            model_name='food',
            name='desc1',
            field=models.TextField(default='1', verbose_name='Image 1 Description'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='food',
            name='desc2',
            field=models.TextField(blank=True, help_text='Only required if image 2 is uploaded', null=True, verbose_name='Image 2 Description'),
        ),
        migrations.AddField(
            model_name='food',
            name='desc3',
            field=models.TextField(blank=True, help_text='Only required if image 3 is uploaded', null=True, verbose_name='Image 3 Description'),
        ),
        migrations.AddField(
            model_name='food',
            name='desc4',
            field=models.TextField(blank=True, help_text='Only required if image 4 is uploaded', null=True, verbose_name='Image 4 Description'),
        ),
        migrations.AddField(
            model_name='food',
            name='desc5',
            field=models.TextField(blank=True, help_text='Only required if image 5 is uploaded', null=True, verbose_name='Image 5 Description'),
        ),
        migrations.AddField(
            model_name='food',
            name='image1',
            field=models.ImageField(default='1', upload_to='images/food', verbose_name='Image 1'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='food',
            name='image2',
            field=models.ImageField(blank=True, help_text='Optional', null=True, upload_to='images/food', verbose_name='Image 2'),
        ),
        migrations.AddField(
            model_name='food',
            name='image3',
            field=models.ImageField(blank=True, help_text='Optional', null=True, upload_to='images/food', verbose_name='Image 3 Description'),
        ),
        migrations.AddField(
            model_name='food',
            name='image4',
            field=models.ImageField(blank=True, help_text='Optional', null=True, upload_to='images/food', verbose_name='Image 4 Description'),
        ),
        migrations.AddField(
            model_name='food',
            name='image5',
            field=models.ImageField(blank=True, help_text='Optional', null=True, upload_to='images/food', verbose_name='Image 5 Description'),
        ),
        migrations.AddField(
            model_name='music',
            name='desc1',
            field=models.TextField(default='1', verbose_name='Image 1 Description'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='music',
            name='desc2',
            field=models.TextField(blank=True, help_text='Only required if image 2 is uploaded', null=True, verbose_name='Image 2 Description'),
        ),
        migrations.AddField(
            model_name='music',
            name='desc3',
            field=models.TextField(blank=True, help_text='Only required if image 3 is uploaded', null=True, verbose_name='Image 3 Description'),
        ),
        migrations.AddField(
            model_name='music',
            name='desc4',
            field=models.TextField(blank=True, help_text='Only required if image 4 is uploaded', null=True, verbose_name='Image 4 Description'),
        ),
        migrations.AddField(
            model_name='music',
            name='desc5',
            field=models.TextField(blank=True, help_text='Only required if image 5 is uploaded', null=True, verbose_name='Image 5 Description'),
        ),
        migrations.AddField(
            model_name='music',
            name='image1',
            field=models.ImageField(default='1', upload_to='images/music', verbose_name='Image 1'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='music',
            name='image2',
            field=models.ImageField(blank=True, help_text='Optional', null=True, upload_to='images/music', verbose_name='Image 2'),
        ),
        migrations.AddField(
            model_name='music',
            name='image3',
            field=models.ImageField(blank=True, help_text='Optional', null=True, upload_to='images/music', verbose_name='Image 3 Description'),
        ),
        migrations.AddField(
            model_name='music',
            name='image4',
            field=models.ImageField(blank=True, help_text='Optional', null=True, upload_to='images/music', verbose_name='Image 4 Description'),
        ),
        migrations.AddField(
            model_name='music',
            name='image5',
            field=models.ImageField(blank=True, help_text='Optional', null=True, upload_to='images/music', verbose_name='Image 5 Description'),
        ),
        migrations.AddField(
            model_name='weddings',
            name='desc1',
            field=models.TextField(default='1', verbose_name='Image 1 Description'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='weddings',
            name='desc2',
            field=models.TextField(blank=True, help_text='Only required if image 2 is uploaded', null=True, verbose_name='Image 2 Description'),
        ),
        migrations.AddField(
            model_name='weddings',
            name='desc3',
            field=models.TextField(blank=True, help_text='Only required if image 3 is uploaded', null=True, verbose_name='Image 3 Description'),
        ),
        migrations.AddField(
            model_name='weddings',
            name='desc4',
            field=models.TextField(blank=True, help_text='Only required if image 4 is uploaded', null=True, verbose_name='Image 4 Description'),
        ),
        migrations.AddField(
            model_name='weddings',
            name='desc5',
            field=models.TextField(blank=True, help_text='Only required if image 5 is uploaded', null=True, verbose_name='Image 5 Description'),
        ),
        migrations.AddField(
            model_name='weddings',
            name='image1',
            field=models.ImageField(default='1', upload_to='images/weddings', verbose_name='Image 1'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='weddings',
            name='image2',
            field=models.ImageField(blank=True, help_text='Optional', null=True, upload_to='images/weddings', verbose_name='Image 2'),
        ),
        migrations.AddField(
            model_name='weddings',
            name='image3',
            field=models.ImageField(blank=True, help_text='Optional', null=True, upload_to='images/weddings', verbose_name='Image 3 Description'),
        ),
        migrations.AddField(
            model_name='weddings',
            name='image4',
            field=models.ImageField(blank=True, help_text='Optional', null=True, upload_to='images/weddings', verbose_name='Image 4 Description'),
        ),
        migrations.AddField(
            model_name='weddings',
            name='image5',
            field=models.ImageField(blank=True, help_text='Optional', null=True, upload_to='images/weddings', verbose_name='Image 5 Description'),
        ),
    ]