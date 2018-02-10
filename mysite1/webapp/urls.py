# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import views
from django.conf.urls import url

urlpatterns = [
url(r'^$',views.index,name='index')
]



# Create your views here.
