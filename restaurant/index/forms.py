from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email_id = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    birth_date = forms.DateField(help_text='Required. Format: YYYY-MM-DD') 
    address = forms.CharField(max_length=250, required=False, help_text='Optional.')
    contact = forms.CharField(max_length=10, required=False, help_text='Optional.')
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email_id','birth_date','address','contact','password1', 'password2', )

class RestaurantForm(UserCreationForm):
	Restaurant_name = forms.CharField(max_length=250, help_text='Required.')
	Restaurant_address = forms.CharField(max_length=250, help_text='Required.')
	gstin = forms.IntegerField(help_text='Required.')
	Restaurant_cuisine = forms.CharField(max_length=250,help_text='Required.')
	Owner_name = forms.CharField(max_length=150,help_text='Required.')
	class Meta:
		model = User
		fields = ('username','Restaurant_name','Restaurant_address','gstin','Restaurant_cuisine','Owner_name','password1',)
