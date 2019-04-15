from django.conf.urls import url

from .views import get_home, get_page, get_project

urlpatterns = [
    url(r'^$', get_home, name='home'),

    # Category Pages
    url(r'^(?P<category>[-\w]+)/$', get_page, name='category'),
    # Project Pages
    url(r'^(?P<category>[-\w]+)/(?P<project_id>\d+)/$', get_project, name='project')
]