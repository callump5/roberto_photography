from django.conf.urls import url

from .views import get_home, get_portraits

urlpatterns = [
    url(r'^$', get_home, name='home'),

    # Portraits

    url(r'^portraits/$', get_portraits, name='portraits'),
]