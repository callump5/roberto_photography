# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Project, Category, Facebook, Instagram, Email, Phone, HomeMusic
# Create your views here.

def get_home(request):
    categories = Category.objects.all()
    projects = Project.objects.all()

    facebook = Facebook.objects.get(pk=1)
    insta = Instagram.objects.get(pk=1)
    phone = Phone.objects.get(pk=1)
    email = Email.objects.get(pk=1)
    music = HomeMusic.objects.get(pk=1)

    args = {
        'facebook': facebook,
        'insta': insta,
        'phone': phone,
        'email': email,
        'categories': categories,
        'projects': projects,
        'music': music
    }

    return render(request, 'home/home-page.html', args)


def get_page(request, category):

    categories = Category.objects.all()
    projects = Project.objects.all()

    facebook = Facebook.objects.get(pk=1)
    insta = Instagram.objects.get(pk=1)
    phone = Phone.objects.get(pk=1)
    email = Email.objects.get(pk=1)
    music = HomeMusic.objects.get(pk=1)

    args = {
        'facebook': facebook,
        'insta': insta,
        'phone': phone,
        'email': email,
        'categories': categories,
        'projects': projects,
        'music': music
    }

    return render(request, 'gallery/gallery.html', args)

