# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Portraits
# Create your views here.

def get_home(request):
    return render(request, 'home/home-page.html')


def get_portraits(request):

    portraits = Portraits.objects.all()

    args = {
        'portraits': portraits
    }
    return render(request, 'portraits/gallery.html', args)

