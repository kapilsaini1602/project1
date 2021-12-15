# -*- coding: utf-8 -*-
# from __future__ import unicode_literals

from django.shortcuts import render,redirect
from homepg.models import Insert
from .forms import UpdateForm
# Create your views here.
def update(request):
    id = request.GET.get('id')
    name = request.POST.get('name')
    designation = request.POST.get('designation')
    contact = request.POST.get('contact')

    obj_all = Insert.objects.filter(id=id)
    obj_index = Insert.objects.all()
    if request.method == 'POST':
        obj = Insert.objects.get(id=id)
        obj.name=name
        obj.Designation=designation
        obj.contact=int(contact)
        obj.save()
        return redirect("http://127.0.0.1:8000/display", {'disp': obj_index})
    return render(request,'update/update.html',{'obj':obj_all})