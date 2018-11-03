# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from index.models import restaurants,rest_menu,reviews
from user_profile.models import userprofile
from .forms import ReviewForm,RestaurantForm
from django.http import HttpResponseRedirect
from django.http import HttpResponse
# Create your views here.
def list(request):
	all_rest = restaurants.objects.all()
	#print all_rest
	return render(request,'list.html',{'all_rest' : all_rest})

def restreg(request):
    # all_rest = restaurants.objects.all()
    if request.method == 'POST':
    	form = RestaurantForm(request.POST,request.FILES)
    	if form.is_valid():
    		form.save()
    		return  redirect('rest_page:list')
    else:
    	form = 	RestaurantForm()
    return render(request,'signupasrest.html',{'form' : form})

def details(request,pk):
	detail = restaurants.objects.get(pk=pk)
	return render(request,'detail.html',{'detail':detail})		

def review(request,pk):
	#detail = restaurants.objects.get(pk=pk)
	if request.method == 'POST':
		form = ReviewForm(request.POST)
		if form.is_valid():
			x = form.save(commit=False)
			detail = restaurants.objects.get(pk=pk)
			x.gstin=detail
			y = request.user.userprofile
			x.userpk=y
			#print(request.user)
			x.save()
			return HttpResponseRedirect('thanks')
	else:
		form = ReviewForm()
	return render(request,'review.html',{'form':form})			

def thanks(request,pk):
	detail = restaurants.objects.get(pk=pk)
	return render(request,'thanks.html',{'detail':detail})

