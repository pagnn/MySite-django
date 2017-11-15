from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,get_user_model
from .forms import LoginForm,RegisterForm,UserProfileForm
User=get_user_model()
# Create your views here.
def user_login(request):
	if request.method == 'POST':
		login_form=LoginForm(request.POST)
		if login_form.is_valid():
			cd=login_form.cleaned_data
			user=authenticate(username=cd['username'],password=cd['password'])
			if user:
				login(request,user)
				return HttpResponse('Successfully Logged.')
			else:
				return HttpResponse('Sorry,your username and password are not right.')
		else:
			return HttpResponse('Invalid Login.')
	if request.method == 'GET':
		login_form=LoginForm()
		return render(request,'account/login.html',{'form':login_form})


def register(request):
	if request.method == 'POST':
		user_form=RegisterForm(request.POST)
		userprofile_form=UserProfileForm(request.POST)
		if user_form.is_valid()*userprofile_form.is_valid():
			new_user=user_form.save(commit=False)
			new_user.set_password(user_form.cleaned_data['password'])
			new_user.save()
			new_profile = userprofile_form.save(commit=False)
			new_profile.user=new_user
			new_profile.save()
			print('saved')
			return HttpResponse('Successfully')
		else:
			return HttpResponse("Sorry,you can't register.")
	if request.method == 'GET':
		user_form=RegisterForm()
		userprofile_form=UserProfileForm()
		return render(request,'account/register.html',{'form':user_form,'profile':userprofile_form})