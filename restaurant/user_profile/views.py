from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .models import userprofile
from .forms import SignUpForm,DetailsForm
from django.contrib.auth.decorators import login_required


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('fill_form')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

@login_required
def view_profile(request):
     # current_user = request.user
     current_user = userprofile.objects.get(user = request.user)
     return render(request,'profile.html', {'profile' : current_user})

@login_required
def fill_form(request):
	try: 
		if (request.user.userprofile):
			return redirect('rest_page:list')
	except:		
		if request.method=='POST':
			form = DetailsForm(request.POST)
			if form.is_valid():
				form.instance.user=request.user
				form.save()
				return redirect('rest_page:list')
		else:
			form = DetailsForm()
	return render(request,'signup.html',{'form' : form})

