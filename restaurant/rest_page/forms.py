from django.forms import ModelForm
from index.models import reviews,restaurants,rest_menu

class ReviewForm(ModelForm):
	#ratings = forms.IntegerField()
	#Feedback = forms.CharField(max_length=254, help_text = 'Mandatory.')


	class Meta:
		model = reviews
		fields = ['ratings','Feedback','gstin',]

class RestaurantForm(ModelForm):

 	class Meta:
 		model = restaurants
 		fields = ['gstin','name','dno','street','city','phn','images',]	

class MenuForm(ModelForm):
 	class Meta:
 		model = rest_menu
 		fields = ['food','price','cuisine',]
