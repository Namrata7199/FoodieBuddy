from django.conf.urls import url,include
from django.contrib import admin
from . import views

app_name = 'rest_page'

urlpatterns = [
	url(r'^$',views.list,name="list"),
]