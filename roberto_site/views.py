# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib import messages


from smtplib import SMTPAuthenticationError

from .send_email import send_contact_request, authError
from .forms import ContactForm
from .models import Project, Category, Facebook, Instagram, Email, Phone, HomeMusic, Background
# Create your views here.

def get_home(request):
    categories = Category.objects.all()
    projects = Project.objects.all()

    facebook = Facebook.objects.all().first()
    insta = Instagram.objects.all().first()
    phone = Phone.objects.all().first()
    email = Email.objects.all().first()
    music = HomeMusic.objects.filter(active=True).first()
    background = Background.objects.filter().first()


    if request.method == 'POST':

        contact_request = ContactForm(request.POST)

        if contact_request.is_valid():
            contact_form = contact_request.save()
            contact_form.save()
            messages.success(request, 'Thanks for getting in touch! We will try to contact you as soon as possible!')
            try:
                send_contact_request(request, contact_form.name, contact_form.email, contact_form.number, contact_form.message)
            except SMTPAuthenticationError:
                authError(request)
        else:
            return redirect('home')

    else:
        contact_request = ContactForm()

    args = {
        'facebook': facebook,
        'insta': insta,
        'phone': phone,
        'email': email,
        'categories': categories,
        'projects': projects,
        'music': music,
        'form': contact_request,
        'background': background
    }

    return render(request, 'home/home-page.html', args)


def get_page(request, category):

    categories = Category.objects.all()
    projects = Project.objects.filter(category__title__exact=category).all()

    facebook = Facebook.objects.all().first()
    insta = Instagram.objects.all().first()
    phone = Phone.objects.all().first()
    email = Email.objects.all().first()
    music = HomeMusic.objects.filter(active=True).first()
    background = Background.objects.filter().first()


    args = {
        'facebook': facebook,
        'insta': insta,
        'phone': phone,
        'email': email,
        'categories': categories,
        'projects': projects,
        'music': music,
        'background': background
    }

    return render(request, 'gallery/gallery.html', args)


def get_project(request, category, project_id):


    categories = Category.objects.all()
    facebook = Facebook.objects.all().first()
    insta = Instagram.objects.all().first()
    phone = Phone.objects.all().first()
    email = Email.objects.all().first()
    music = HomeMusic.objects.filter(active=True).first()


    project_category = Category.objects.filter(title__exact=category).first()

    project = Project.objects.get(pk=project_id)


    args = {
        'facebook': facebook,
        'insta': insta,
        'phone': phone,
        'email': email,
        'categories': categories,
        'category': project_category,
        'project': project,
        'music': music,
    }


    return render(request, 'gallery/project-details.html', args)