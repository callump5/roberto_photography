from django.conf.urls import url

from .views import get_home, get_page

urlpatterns = [
    url(r'^$', get_home, name='home'),

    # Portraits

    url(r'^(?P<category>[-\w]+)/$', get_page, name='project'),
]