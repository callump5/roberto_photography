# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.timezone import now


import os


# Create your models here.

class Category(models.Model):
    title = models.CharField(u'Category Title', max_length=300)
    description = models.TextField(u'Category Description')

    def __unicode__(self):
        return self.title

    class Meta():
        verbose_name = 'Portfolio Category'
        verbose_name_plural = 'Categories'



class Project(models.Model):
    title = models.CharField(max_length=400)

    category = models.ForeignKey(Category)

    image1 = models.ImageField(u'Image 1', upload_to='images/gallery')
    desc1 = models.TextField(u'Image 1 Description')

    image2 = models.ImageField(u'Image 2', upload_to='images/gallery', blank=True, null=True, help_text='Optional')
    desc2 = models.TextField(u'Image 2 Description',blank=True, null=True, help_text='Only required if image 2 is uploaded')

    image3 = models.ImageField(u'Image 3 Description', upload_to='images/gallery', blank=True, null=True, help_text='Optional')
    desc3 = models.TextField(u'Image 3 Description', blank=True, null=True, help_text='Only required if image 3 is uploaded')

    image4 = models.ImageField(u'Image 4 Description', upload_to='images/gallery', blank=True, null=True, help_text='Optional')
    desc4 = models.TextField(u'Image 4 Description', blank=True, null=True, help_text='Only required if image 4 is uploaded')

    image5 = models.ImageField(u'Image 5 Description', upload_to='images/gallery', blank=True, null=True, help_text='Optional')
    desc5 = models.TextField(u'Image 5 Description',blank=True, null=True, help_text='Only required if image 5 is uploaded')

    def __unicode__(self):
        return self.title +  '-' + str(self.category)

    class Meta():
        verbose_name = 'Project'
        verbose_name_plural = 'Project'
