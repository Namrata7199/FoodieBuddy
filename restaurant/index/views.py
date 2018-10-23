# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from .forms import SignUpForm
from django.shortcuts import render, redirect

# Create your views here.
def home(request):
	return render(request,'home.html')

def signupasuser(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.birth_date = form.cleaned_data.get('birth_date')
            user.profile.first_name = form.cleaned_data.get('first_name')
            user.profile.last_name = form.cleaned_data.get('last_name')
            user.profile.email_id = form.cleaned_data.get('email_id')
            user.profile.address = form.cleaned_data.get('address')
            user.profile.contact = form.cleaned_data.get('contact')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signupasuser.html', {'form': form})	
    
def signupasrest(request):
    if request.method == 'POST':
        form = RestaurantForm(request.POST)
        if form.is_valid():
            rest = form.save()
            rest.refresh_from_db()
            user.profile.Restaurant_name = form.cleaned_data.get('Restaurant_name')
            rest.profile.Restaurant_address = form.cleaned_data.get('Restaurant_address')
            rest.profile.gstin = form.cleaned_data.get('gstin')
            rest.profile.Owner_name = form.cleaned_data.get('Owner_name')
            rest.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, rest)
            return redirect('home')
    else:
        form = RestaurantForm()
    return render(request, 'signupasrest.html',{'form':form})    

	

