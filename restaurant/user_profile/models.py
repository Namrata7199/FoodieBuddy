# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User


from django.db import models

# Create your models here.
class userprofile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	street = models.CharField(max_length=30)
	city = models.CharField(max_length=30)
	phn = models.CharField(max_length=10)
	