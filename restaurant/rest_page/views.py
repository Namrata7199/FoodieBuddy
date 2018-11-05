# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from index.models import restaurants,rest_menu,reviews,owner
from index.models import restaurants,rest_menu,reviews
from user_profile.models import userprofile
from .forms import ReviewForm,RestaurantForm
from .forms import ReviewForm,RestaurantForm,MenuForm
from django.http import HttpResponseRedirect
from django.http import HttpResponse
# Create your views here.
def list(request):
	all_rest = restaurants.objects.all()
	return render(request,'list.html',{'all_rest' : all_rest})

def restreg(request):
    if request.method == 'POST':
    	form = RestaurantForm(request.POST,request.FILES)
    	print(form)
    	if form.is_valid():
    		rest = form.save(commit=False)
    		x = owner()
    		x.user = request.user
    		x.save()
    		rest.userpk = x
    		rest.save()
    		return  redirect('rest_page:add_menu', pk=rest.pk)
    else:
    	form = 	RestaurantForm()
    return render(request,'add_restaurant.html',{'form' : form})

def details(request,pk):
	detail = restaurants.objects.get(pk=pk)
	user = request.user
	return render(request,'detail.html',{'detail':detail, 'user': user})		

def review(request,pk):
	if request.method == 'POST':
		form = ReviewForm(request.POST)
		if form.is_valid():
			x = form.save(commit=False)
			detail = restaurants.objects.get(pk=pk)
			x.gstin=detail
			y = request.user.userprofile
			x.userpk=y
			x.save()
			return HttpResponseRedirect('thanks')
	else:
		form = ReviewForm()
		detail = restaurants.objects.get(pk=pk)
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

def search_by_name(request):
	if request.method == "POST":
		name = request.POST['name']
		if name:
			data = restaurants.objects.filter(name=name)
			return render(request, 'list.html', {'all_rest': data})
		else:
			return redirect('rest_page:list')       
	else:
		return redirect('rest_page:list')					

def search_by_cuisine(request):
	if request.method == "POST":
		name = request.POST['cuisine']
		res = []
		if name:
			for x in restaurants.objects.all():
				for y in x.menupk.all():
					if name==y.cuisine:
						res.append(x)
						break;
			return render(request, 'list.html', {'all_rest': res})
		else:
			return redirect('rest_page:list')       
	else:
		return redirect('rest_page:list')					
