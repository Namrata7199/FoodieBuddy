# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from user_profile.models import userprofile
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class rest_menu(models.Model):
	food = models.CharField(max_length=30)
	price = models.IntegerField()
	cuisine = models.CharField(max_length=20)

class owner(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)


class restaurants(models.Model):
	gstin = models.CharField(primary_key=True,max_length=20)
	name = models.CharField(max_length=30)
	dno = models.CharField(max_length=10)
	street = models.CharField(max_length=30)
	city = models.CharField(max_length=30)
	phn = models.CharField(max_length=10)
	images = models.ImageField(upload_to = 'media/')
	menupk = models.ManyToManyField(rest_menu)
	userpk = models.ForeignKey(owner,on_delete=models.CASCADE, blank=True)


class reviews(models.Model):
	ratings = models.IntegerField()
	Feedback = models.CharField(max_length=1000)
	gstin = models.ForeignKey(restaurants,on_delete=models.CASCADE,blank=True)
	userpk = models.ForeignKey(userprofile,on_delete=models.CASCADE,blank=True)




    
