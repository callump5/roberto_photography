# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


# Background Image

class Background(models.Model):
    image = models.ImageField(u'Background Image', upload_to='images/background')


    def __unicode__(self):
        return 'Background Image'

    class Meta():
        verbose_name = 'Background Image'
        verbose_name_plural = 'Background images'


# Social Links

class Facebook(models.Model):
    link = models.CharField(max_length=600)


    def __unicode__(self):
        return 'Facebook Link'

    class Meta():
        verbose_name = 'Facebook Links'
        verbose_name_plural = 'FB Links'


class Instagram(models.Model):
    link = models.CharField(max_length=600)


    def __unicode__(self):
        return 'Instagram Link'

    class Meta():
        verbose_name = 'Instagram Links'
        verbose_name_plural = 'Insta Links'

class Email(models.Model):
    link = models.CharField(max_length=600)


    def __unicode__(self):
        return 'Email Address'

    class Meta():
        verbose_name = 'Email Address'
        verbose_name_plural = 'Email'

class Phone(models.Model):
    link = models.CharField(max_length=600)


    def __unicode__(self):
        return 'Phone Number'

    class Meta():
        verbose_name = 'Phone Number'
        verbose_name_plural = 'Phone'


# Site Music

class HomeMusic(models.Model):
    song = models.FileField()
    active = models.BooleanField()


    def __unicode__(self):
        return 'Music'

    class Meta():
        verbose_name = 'Music'
        verbose_name_plural = 'Songs'



# Contact Request

class ContactRequest(models.Model):
    name = models.CharField(u'Full Name', help_text='Please enter your full name', max_length=400)
    number = models.CharField(u'Contact Number', help_text='Please enter your contact number', max_length=11)
    email = models.CharField(u'Email Address', help_text='Please enter your Email address', max_length=400)
    message = models.TextField(u'Message', help_text='How can I help?')

    def __unicode__(self):
        return self.name

    class Meta():
        verbose_name = 'Contact Request'
        verbose_name_plural ='Contact Requests'



# Project Category

class Category(models.Model):
    title = models.CharField(u'Category Title', max_length=300)
    description = models.TextField(u'Category Description')

    def __unicode__(self):
        return self.title

    class Meta():
        verbose_name = 'Portfolio Category'
        verbose_name_plural = 'Categories'


# Projects

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
