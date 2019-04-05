# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.timezone import now


import os


# Create your models here.

class Portraits(models.Model):
    title = models.CharField(max_length=400)

    image1 = models.ImageField(u'Image 1', upload_to='images/portraits')
    desc1 = models.TextField(u'Image 1 Description')

    image2 = models.ImageField(u'Image 2', upload_to='images/portraits', blank=True, null=True, help_text='Optional')
    desc2 = models.TextField(u'Image 2 Description',blank=True, null=True, help_text='Only required if image 2 is uploaded')

    image3 = models.ImageField(u'Image 3 Description', upload_to='images/portraits', blank=True, null=True, help_text='Optional')
    desc3 = models.TextField(u'Image 3 Description', blank=True, null=True, help_text='Only required if image 3 is uploaded')

    image4 = models.ImageField(u'Image 4 Description', upload_to='images/portraits', blank=True, null=True, help_text='Optional')
    desc4 = models.TextField(u'Image 4 Description', blank=True, null=True, help_text='Only required if image 4 is uploaded')

    image5 = models.ImageField(u'Image 5 Description', upload_to='images/portraits', blank=True, null=True, help_text='Optional')
    desc5 = models.TextField(u'Image 5 Description',blank=True, null=True, help_text='Only required if image 5 is uploaded')

    def __unicode__(self):
        return self.title

    class Meta():
        verbose_name = 'Portrait Image'
        verbose_name_plural = 'Portrait Gallery'


class Weddings(models.Model):

    title = models.CharField(max_length=400)

    image1 = models.ImageField(u'Image 1', upload_to='images/weddings')
    desc1 = models.TextField(u'Image 1 Description')

    image2 = models.ImageField(u'Image 2', upload_to='images/weddings', blank=True, null=True, help_text='Optional')
    desc2 = models.TextField(u'Image 2 Description',blank=True, null=True, help_text='Only required if image 2 is uploaded')

    image3 = models.ImageField(u'Image 3 Description', upload_to='images/weddings', blank=True, null=True, help_text='Optional')
    desc3 = models.TextField(u'Image 3 Description', blank=True, null=True, help_text='Only required if image 3 is uploaded')

    image4 = models.ImageField(u'Image 4 Description', upload_to='images/weddings', blank=True, null=True, help_text='Optional')
    desc4 = models.TextField(u'Image 4 Description', blank=True, null=True, help_text='Only required if image 4 is uploaded')

    image5 = models.ImageField(u'Image 5 Description', upload_to='images/weddings', blank=True, null=True, help_text='Optional')
    desc5 = models.TextField(u'Image 5 Description',blank=True, null=True, help_text='Only required if image 5 is uploaded')

    def __unicode__(self):
        return self.title

    class Meta():
        verbose_name = 'Wedding Image'
        verbose_name_plural = 'Wedding Gallery'




class Food(models.Model):
    title = models.CharField(max_length=400)

    image1 = models.ImageField(u'Image 1', upload_to='images/food')
    desc1 = models.TextField(u'Image 1 Description')

    image2 = models.ImageField(u'Image 2', upload_to='images/food', blank=True, null=True, help_text='Optional')
    desc2 = models.TextField(u'Image 2 Description',blank=True, null=True, help_text='Only required if image 2 is uploaded')

    image3 = models.ImageField(u'Image 3 Description', upload_to='images/food', blank=True, null=True, help_text='Optional')
    desc3 = models.TextField(u'Image 3 Description', blank=True, null=True, help_text='Only required if image 3 is uploaded')

    image4 = models.ImageField(u'Image 4 Description', upload_to='images/food', blank=True, null=True, help_text='Optional')
    desc4 = models.TextField(u'Image 4 Description', blank=True, null=True, help_text='Only required if image 4 is uploaded')

    image5 = models.ImageField(u'Image 5 Description', upload_to='images/food', blank=True, null=True, help_text='Optional')
    desc5 = models.TextField(u'Image 5 Description',blank=True, null=True, help_text='Only required if image 5 is uploaded')


    def __unicode__(self):
        return self.title

    class Meta():
        verbose_name = 'Food Image'
        verbose_name_plural = 'Food Gallery'




class Music(models.Model):
    title = models.CharField(max_length=400)

    image1 = models.ImageField(u'Image 1', upload_to='images/music')
    desc1 = models.TextField(u'Image 1 Description')

    image2 = models.ImageField(u'Image 2', upload_to='images/music', blank=True, null=True, help_text='Optional')
    desc2 = models.TextField(u'Image 2 Description',blank=True, null=True, help_text='Only required if image 2 is uploaded')

    image3 = models.ImageField(u'Image 3 Description', upload_to='images/music', blank=True, null=True, help_text='Optional')
    desc3 = models.TextField(u'Image 3 Description', blank=True, null=True, help_text='Only required if image 3 is uploaded')

    image4 = models.ImageField(u'Image 4 Description', upload_to='images/music', blank=True, null=True, help_text='Optional')
    desc4 = models.TextField(u'Image 4 Description', blank=True, null=True, help_text='Only required if image 4 is uploaded')

    image5 = models.ImageField(u'Image 5 Description', upload_to='images/music', blank=True, null=True, help_text='Optional')
    desc5 = models.TextField(u'Image 5 Description',blank=True, null=True, help_text='Only required if image 5 is uploaded')

    def __unicode__(self):
        return self.title

    class Meta():
        verbose_name = 'Music Image'
        verbose_name_plural = 'Music Gallery'




class Families(models.Model):
    title = models.CharField(max_length=400)

    image1 = models.ImageField(u'Image 1', upload_to='images/families')
    desc1 = models.TextField(u'Image 1 Description')

    image2 = models.ImageField(u'Image 2', upload_to='images/families', blank=True, null=True, help_text='Optional')
    desc2 = models.TextField(u'Image 2 Description',blank=True, null=True, help_text='Only required if image 2 is uploaded')

    image3 = models.ImageField(u'Image 3 Description', upload_to='images/families', blank=True, null=True, help_text='Optional')
    desc3 = models.TextField(u'Image 3 Description', blank=True, null=True, help_text='Only required if image 3 is uploaded')

    image4 = models.ImageField(u'Image 4 Description', upload_to='images/families', blank=True, null=True, help_text='Optional')
    desc4 = models.TextField(u'Image 4 Description', blank=True, null=True, help_text='Only required if image 4 is uploaded')

    image5 = models.ImageField(u'Image 5 Description', upload_to='images/families', blank=True, null=True, help_text='Optional')
    desc5 = models.TextField(u'Image 5 Description',blank=True, null=True, help_text='Only required if image 5 is uploaded')

    def __unicode__(self):
        return self.title

    class Meta():
        verbose_name = 'Families Image'
        verbose_name_plural = 'Families Gallery'
