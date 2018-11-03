from django.conf.urls import url,include
from django.contrib import admin
from . import views

app_name = 'rest_page'

urlpatterns = [
	url(r'^$',views.list,name="list"),
	url(r'^restreg/$',views.restreg,name="restreg"),
	url(r'^(?P<pk>[0-9]+)/$',views.details,name="details"),
	url(r'^(?P<pk>[0-9]+)/review/$',views.review,name="review"),
	url(r'^(?P<pk>[0-9]+)/review/thanks/$',views.thanks,name="thanks"),
	url(r'^restreg/(?P<pk>[0-9]+)/$',views.add_menu,name="add_menu"),
	#url(r'^search/$', views.search, name='search'),
]