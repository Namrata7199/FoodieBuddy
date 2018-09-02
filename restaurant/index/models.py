# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class rest_menu(models.Model):
	food = models.CharField(max_length=30)
	price = models.IntegerField()
	cuisine = models.CharField(max_length=20)

class restaurant(models.Model):
	name = models.CharField(max_length=30)
	dno = models.CharField(max_length=10)
	street = models.CharField(max_length=30)
	city = models.CharField(max_length=30)
	phn = models.IntegerField()
	images = models.ImageField(max_length=10000)
	gstin = models.CharField(primary_key=True,max_length=20)
	menupk = models.ForeignKey(rest_menu,on_delete=models.CASCADE)

class owner(models.Model):
	first_name = models.CharField(max_length=30)
	middle_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	gstin = models.ForeignKey(restaurant,on_delete=models.CASCADE)
