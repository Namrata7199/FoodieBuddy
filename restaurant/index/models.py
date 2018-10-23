# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class rest_menu(models.Model):
	food = models.CharField(max_length=30)
	price = models.IntegerField()
	cuisine = models.CharField(max_length=20)

class restaurant(models.Model):
	gstin = models.CharField(primary_key=True,max_length=20)
	name = models.CharField(max_length=30)
	dno = models.CharField(max_length=10)
	street = models.CharField(max_length=30)
	city = models.CharField(max_length=30)
	phn = models.IntegerField()
	images = models.ImageField(max_length=10000)
	menupk = models.ForeignKey(rest_menu,on_delete=models.CASCADE)
	cuisine = models.CharField(max_length=30)

	class meta:
		db_table = 'restaurant'
		unique_together = (('name','dno','street','city','phn','images'),)

class owner(models.Model):
	first_name = models.CharField(max_length=30)
	middle_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	gstin = models.ForeignKey(restaurant,on_delete=models.CASCADE)

class reviews(models.Model):
	ratings = models.IntegerField()
	Feedback = models.CharField(max_length=1000)
	gstin = models.ForeignKey(restaurant,on_delete=models.CASCADE)
	userpk = models.ForeignKey(owner,on_delete=models.CASCADE)

class user(models.Model):
	email = models.CharField(primary_key=True,max_length = 30)
	first_name = models.CharField(max_length=30)
	middle_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	dno = models.CharField(max_length=10)
	street = models.CharField(max_length=30)
	city = models.CharField(max_length=30)
	phn = models.IntegerField()
	rest = models.ForeignKey(restaurant,on_delete=models.CASCADE)

class search_by_cuisine(models.Model):
	gstin = models.ForeignKey(restaurant,on_delete=models.CASCADE)
	email = models.ForeignKey(user,on_delete=models.CASCADE)



    
