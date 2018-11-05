# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
#from .forms import SignUpForm,RestaurantForm
from django.shortcuts import render, redirect
from django.views.generic import View

# Create your views here.
def home(request):
	return render(request,'home.html')

