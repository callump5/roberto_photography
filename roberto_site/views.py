# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Project, Category
# Create your views here.

def get_home(request):
    categories = Category.objects.all()
    projects = Project.objects.all()

    args = {
        'categories': categories,
        'projects': projects
    }

    return render(request, 'home/home-page.html', args)


def get_page(request, category):


    categories = Category.objects.all()
    projects = Project.objects.filter(category__title__exact=category)

    args = {
        'projects': projects,
        'categories': categories,
    }
    return render(request, 'gallery/gallery.html', args)

