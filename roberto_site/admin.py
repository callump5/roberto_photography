# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Facebook, Instagram, Email, Phone, Project, Category, HomeMusic, ContactRequest, Background

# Register your models here.

admin.site.register(Project)
admin.site.register(Category)

admin.site.register(ContactRequest)

admin.site.register(Background)

admin.site.register(Instagram)
admin.site.register(Facebook)
admin.site.register(Phone)
admin.site.register(Email)
admin.site.register(HomeMusic)