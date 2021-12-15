# -*- coding: utf-8 -*-
# from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from homepg.models import Insert

from django.shortcuts import render, HttpResponse, redirect
from .forms import PostForm


# Create your views here.
def home(request):
    if request.method == 'POST':
        context = {}
        fm = PostForm(request.POST, request.FILES)
        image = request.FILES.get('image')
        if fm.is_valid():
            fm.save()
            print(fm)

        else:
            frm = PostForm(request.POST, None)
            print("ELSE",frm)

            context['form'] = frm
            context['frm'] = "*Invalid Contact Number"

            return render(request, 'homepg/homepg.html',context)
            # print(details)
            # from homepg.models import Insert
            # name = request.POST.get('name')
            # desig = request.POST.get('designation')
            # contact = request.POST.get('contact')
            # image = request.FILES['file']
            # insert = Insert.objects.create(name=name,Designation=desig,contact=contact,image=image)
            # insert.save()
        disp = Insert.objects.all()
        return redirect("http://127.0.0.1:8000/display", {'disp': disp, 'form': fm})
    return render(request, 'homepg/homepg.html')


# Uploading images with file system storage.
#     if request.method == "POST":
#         # if the post request has a file under the input name 'document', then save the file.
#         request_file = request.FILES['image'] if 'image' in request.FILES else None
#         if request_file:
#             fs = FileSystemStorage()
#             file = fs.save(request_file.name, request_file)
#             fileurl = fs.url(file)
#             print(fileurl)
#             disp = Insert.objects.all()
#             return redirect("http://127.0.0.1:8000/display", {'disp': disp})
#
#     return render(request, 'homepg/homepg.html')
