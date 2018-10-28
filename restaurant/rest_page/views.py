# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from index.models import restaurants,rest_menu

# Create your views here.
def list(request):
	all_rest = restaurants.objects.all()
	#print all_rest
	return render(request,'list.html',{'all_rest' : all_rest})