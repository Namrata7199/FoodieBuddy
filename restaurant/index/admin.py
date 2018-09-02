# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import rest_menu,restaurant,owner

# Register your models here.
admin.site.register(rest_menu)
admin.site.register(restaurant)
admin.site.register(owner)