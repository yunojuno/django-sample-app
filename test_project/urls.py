# -*- coding: utf-8 -*-
# test_app.urls
from django.conf.urls import patterns, url, include
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns(
    'test_app.views',
    url(
        r'^admin/',
        include(admin.site.urls)
    ),
)
