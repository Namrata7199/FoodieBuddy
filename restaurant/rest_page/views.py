# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from index.models import restaurants,rest_menu,reviews,owner
from .forms import ReviewForm,RestaurantForm,MenuForm
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
    		rest = form.save()
    		x = owner()
    		x.first_name = request.user.first_name
    		x.last_name = request.user.last_name
    		x.gstin = rest
    		x.save()
    		return  redirect('rest_page:add_menu', pk=rest.pk)
    else:
    	form = 	RestaurantForm()
    return render(request,'signupasrest.html',{'form' : form})

def details(request,pk):
	detail = restaurants.objects.get(pk=pk)
	return render(request,'detail.html',{'detail':detail})		

def review(request,pk):
	detail = restaurants.objects.get(pk=pk)
	if request.method == 'POST':
		form = ReviewForm(request.POST)
		if form.is_valid():
			form.save(commit=False)
			return HttpResponseRedirect('thanks')
	else:
		form = ReviewForm()
	return render(request,'review.html',{'form':form,'detail':detail})			

def thanks(request,pk):
	detail = restaurants.objects.get(pk=pk)
	return render(request,'thanks.html',{'detail':detail})

def add_menu(request,pk):
	if request.method=='POST':
		form = MenuForm(request.POST)
		if form.is_valid():
			x = form.save()
			rest = restaurants.objects.get(pk=pk)
			rest.menupk.add(x)
			rest.save()
			return redirect('rest_page:add_menu', pk=pk)
	else:
		form = MenuForm()
	return render(request,'add_menu.html',{'form':form, 'rest_pk':pk})
