# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class rest_menu(models.Model):
	food = models.CharField(max_length=30)
	price = models.IntegerField()
	cuisine = models.CharField(max_length=20)

class restaurants(models.Model):
	gstin = models.CharField(primary_key=True,max_length=20)
	name = models.CharField(max_length=30)
	dno = models.CharField(max_length=10)
	street = models.CharField(max_length=30)
	city = models.CharField(max_length=30)
	phn = models.CharField(max_length=10)
	images = models.ImageField(upload_to = 'media/')
	menupk = models.ManyToManyField(rest_menu)

	class meta:
		db_table = 'restaurants'
		unique_together = (('name','dno','street','city','phn'),)

class owner(models.Model):
	first_name = models.CharField(max_length=30)
	middle_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	gstin = models.ForeignKey(restaurants,on_delete=models.CASCADE)

class reviews(models.Model):
	ratings = models.IntegerField()
	Feedback = models.CharField(max_length=1000)
	gstin = models.ForeignKey(restaurants,on_delete=models.CASCADE)
	userpk = models.ForeignKey(owner,on_delete=models.CASCADE)
# class user(models.Model):
	# email = models.CharField(primary_key=True,max_length = 30)
	# first_name = models.CharField(max_length=30)
	# middle_name = models.CharField(max_length=30)
	# last_name = models.CharField(max_length=30)
	# dno = models.CharField(max_length=10)
	# street = models.CharField(max_length=30)
	# city = models.CharField(max_length=30)
	# phn = models.CharField(max_length=10)
 # 	rest = models.ForeignKey(restaurants,on_delete=models.CASCADE)
	# phn = models.IntegerField()
	# rest = models.ForeignKey(restaurants,on_delete=models.CASCADE)

# class search_by_cuisine(models.Model):
# 	gstin = models.ForeignKey(restaurants,on_delete=models.CASCADE)
# 	email = models.ForeignKey(user,on_delete=models.CASCADE)



    
