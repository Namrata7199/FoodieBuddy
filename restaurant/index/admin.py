# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import rest_menu,restaurants,owner,reviews

# Register your models here.
admin.site.register(rest_menu)
admin.site.register(restaurants)
admin.site.register(owner)
#admin.site.register(user)
admin.site.register(reviews)
#admin.site.register(search_by_cuisine)
