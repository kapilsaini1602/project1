# -*- coding: utf-8 -*-
# from __future__ import unicode_literals

from django.shortcuts import render,redirect
from homepg.models import *
# Create your views here.
def delete(request):
    disp = Insert.objects.all()
    id = request.GET.get('id')
    obj = Insert.objects.get(id=id).delete()
    return redirect("http://127.0.0.1:8000/display")

    return render(request,'displ/displ.html',{'disp':disp})
