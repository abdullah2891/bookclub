# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import generics
from .models import BookList
from .serializers import BooklistSerializer
# Create your views here.

class CreateView(generics.ListCreateAPIView): 
    queryset = BookList.objects.all()
    serializer_class = BooklistSerializer
    
    def perform_create(self, serializer): 
        serializer.save()


class DetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BookList.objects.all()
    
    serializer_class = BooklistSerializer 
    
    