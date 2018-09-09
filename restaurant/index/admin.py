# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import rest_menu,restaurant,owner,user,reviews,search_by_cuisine

# Register your models here.
admin.site.register(rest_menu)
admin.site.register(restaurant)
admin.site.register(owner)
admin.site.register(user)
admin.site.register(reviews)
admin.site.register(search_by_cuisine)
