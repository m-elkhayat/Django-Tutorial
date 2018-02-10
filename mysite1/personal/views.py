# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
	return render(request,'personal/home.html')
def contact(request):
	return render(request,'personal/contact.html',{'context':['Mahmoud FAthallah Abu El soud Elsaid Elkhayat','Elkhayat.fci.it@gmail.com']})
