# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.timezone import now


import os


# Create your models here.

class Portraits(models.Model):
    title = models.CharField(max_length=400)
    image = models.ImageField(upload_to='images/portraits')
    description = models.TextField()

    def __unicode__(self):
        return self.title

    class Meta():
        verbose_name = 'Portrait Image'
        verbose_name_plural = 'Portrait Gallery'


class Weddings(models.Model):
    title = models.CharField(max_length=400)
    image = models.ImageField(upload_to='images/weddings')
    description = models.TextField()

    def __unicode__(self):
        return self.title

    class Meta():
        verbose_name = 'Wedding Image'
        verbose_name_plural = 'Wedding Gallery'

class Food(models.Model):
    title = models.CharField(max_length=400)
    image = models.ImageField(upload_to='images/food')
    description = models.TextField()

    def __unicode__(self):
        return self.title

    class Meta():
        verbose_name = 'Food Image'
        verbose_name_plural = 'Food Gallery'

class Music(models.Model):
    title = models.CharField(max_length=400)
    image = models.ImageField(upload_to='images/music')
    description = models.TextField()

    def __unicode__(self):
        return self.title

    class Meta():
        verbose_name = 'Music Image'
        verbose_name_plural = 'Music Gallery'

class Families(models.Model):
    title = models.CharField(max_length=400)
    image = models.ImageField(upload_to='images/families')
    description = models.TextField()

    def __unicode__(self):
        return self.title

    class Meta():
        verbose_name = 'Families Image'
        verbose_name_plural = 'Families Gallery'
