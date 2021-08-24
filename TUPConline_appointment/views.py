from django.shortcuts import render, redirect
from django.http import HttpResponse
from django import forms
from .forms import ScheduleForm, StatusForm, CreateUserForm
from .models import schedule
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .decorators import allowed_users, unauthenticated_user
from django.contrib.auth.models import Group

@unauthenticated_user
def registerPage(request):
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				user = form.save()
				username = form.cleaned_data.get('username')

				group = Group.objects.get(name='Visitor')
				user.groups.add(group)

				messages.success(request, 'Account was created for ' + username)

				return redirect('/login')
			

		context = {'form':form}
		return render(request, 'register.html', context)

@unauthenticated_user
def loginPage(request):

		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('/main')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'login.html', context)


def logoutUser(request):
	logout(request)
	return redirect('login')
def Main(request):
	return render(request, '1st.html')
	
@login_required(login_url='login')
def make(request):
	
	form = ScheduleForm()
	if request.method == 'POST':		
		form = ScheduleForm (request.POST)
		if form.is_valid():
			form.save()
			return redirect('/home')
			
	context = {'form':form}

	return render(request, 'apointment.html', context)
@login_required(login_url='login')
@allowed_users(allowed_roles=['Visitor'])
def home(request):
	visit = schedule.objects.all()
	
	context = {'visit':visit}

	return render(request, 'userhome.html', context)


#dito si admin lang makakapasok
@allowed_users(allowed_roles=['Admin'])
def depthome(request):
	dhome = schedule.objects.all()
	accept = dhome.filter(status='Accept').count()
	deny = dhome.filter(status='Deny').count()
	pending = dhome.filter(status='Pending').count()
	form = StatusForm()
	if request.method == 'POST':		
		form = StatusForm(request.POST)
		if form.is_valid():
			form.save()
			#return redirect('/home')
			return redirect('/dhome')
	context = {'form':form,'dhome': dhome, 'accept': accept, 'deny': deny, 'pending': pending}


	return render(request, 'departmenthome.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin'])
def update(request, pk):

	user = schedule.objects.get(id=pk)
	form = StatusForm(instance=user)

	if request.method == 'POST':
		form = StatusForm(request.POST, instance=user)
		if form.is_valid():
			form.save()
			return redirect('/dhome')

	context = {'form':form}
	return render(request, 'sign.html', context)
