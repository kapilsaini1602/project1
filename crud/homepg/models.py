# -*- coding: utf-8 -*-
# from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Insert(models.Model):
    name = models.CharField(max_length=30)
    Designation = models.CharField(max_length=30)
    contact = models.IntegerField()
    image = models.ImageField(upload_to='images', null=True)
