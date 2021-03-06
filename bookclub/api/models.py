# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class BookList(models.Model): 
    name = models.CharField(max_length=255 , blank=False, unique=True)
    date_created = models.DateTimeField(auto_now_add = True)
    date_modified= models.DateTimeField(auto_now = True)
    
    
    def __str__(self): 
        print self
        return "{}".format(self.name)