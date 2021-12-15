# -*- coding: utf-8 -*-
# from __future__ import unicode_literals

from django.shortcuts import render
from homepg.models import *

# Create your views here.
def display(request):
    disp = Insert.objects.all()
    return render(request,'displ/displ.html',{'disp':disp})