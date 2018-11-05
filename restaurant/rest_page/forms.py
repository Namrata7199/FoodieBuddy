from django.forms import ModelForm
from index.models import reviews,restaurants,rest_menu

class ReviewForm(ModelForm):
	class Meta:
		model = reviews
		fields = ['ratings','Feedback',]

class RestaurantForm(ModelForm):

 	class Meta:
 		model = restaurants
 		fields = ['gstin','name','dno','street','city','phn','images',]	

class MenuForm(ModelForm):
 	class Meta:
 		model = rest_menu
 		fields = ['food','price','cuisine',]
