from django.shortcuts import render, redirect
from . import forms
from django.contrib.auth import login, logout, authenticate

# Create your views here.
def index_home(request):
	return render(request, 'web/home.html')

def sign_up(request):
	if request.method == "POST":
		form = forms.UserRegistrationForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			return redirect("/event")
	else:
		form = forms.UserRegistrationForm()

	return render(request, "registration/sign-up.html", {"form" : form})