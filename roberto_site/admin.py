# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Portraits, Weddings, Food, Music, Families

# Register your models here.

admin.site.register(Portraits)
admin.site.register(Weddings)
admin.site.register(Food)
admin.site.register(Music)
admin.site.register(Families)