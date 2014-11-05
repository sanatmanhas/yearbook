from django.shortcuts import render, render_to_response, RequestContext, HttpResponseRedirect
from django.core.urlresolvers import reverse
from .forms import SignUpForm
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Entry
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.db import IntegrityError
from django.utils.datastructures import MultiValueDictKeyError
import os

# Create your views here.
def home(request):
	return render_to_response("home.html",
						  locals(),
						  context_instance=RequestContext(request))

def logout(request):
	auth_logout(request)
	return HttpResponseRedirect(reverse('home'))

def signup(request):
	form = SignUpForm(request.POST or None)
	if form.is_valid():
		first_name = request.POST['first_name']
		last_name  = request.POST['last_name']
		email	   = request.POST['email']
		password   = request.POST['password']
		username   = request.POST['username']
		user = User.objects.create_user(first_name, email, password)
		user.first_name = first_name
		user.last_name  = last_name
		user.username   = username
		
		user.save()
		
		messages.add_message(request, messages.SUCCESS, 'Sign Up successful. You can now log in with your username/password.')
		return HttpResponseRedirect(reverse('home'))
	return render_to_response("signup.html",
						  locals(),
						  context_instance=RequestContext(request))

def login(request):
	if request.method == 'POST':
		passwd   = request.POST['password']
		usrnm    = request.POST['username']
		user = authenticate(username=usrnm, password=passwd)
		if user:
			# password verified
			if user.is_active:
				auth_login(request, user)
				messages.add_message(request, messages.SUCCESS, 'You have successfully logged in.')
				return HttpResponseRedirect(reverse('home'))
			else:
				messages.add_message(request, messages.WARNING, 'Your account has been deactivated. Contact the admin for reactivation.')
				return HttpResponseRedirect(reverse('home'))
		else:
			# invalid password
			messages.add_message(request, messages.ERROR, 'Invalid username/password')
			return HttpResponseRedirect(reverse('home'))
	if request.method == 'GET':
		return render_to_response("login.html",
								  locals(),
								  context_instance=RequestContext(request))

def users(request):
	if request.method == 'POST':
		try:
			content = request.POST['content']
		except MultiValueDictKeyError:
			messages.add_message(request, messages.ERROR, 'Post content cant be empty')
			return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
		if content == '':
			messages.add_message(request, messages.ERROR, 'Yearbook entry cant be blank!')
			return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
		rec = User.objects.get(username=request.GET['user'])
		sen = request.user
		entry = Entry(sender=sen, recipient=rec, content=content)
		entry.save()
		messages.add_message(request, messages.SUCCESS, 'Successfully wrote in ' + rec.username + "'s yearbook!")
		return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
	try:
		usr = request.GET['user']
	except MultiValueDictKeyError:
		usr = None
	# no user argument; list all users
	if not usr:
		users = User.objects.all()
		return render_to_response("users.html",
								  locals(),
								  context_instance=RequestContext(request))
	else:
		profile_user = User.objects.get(username=usr)
		if os.path.isfile(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'static', 'static', 'images', profile_user.username + '.jpg')):
			var = profile_user.username
		else:
			var = 'User-Default'
		entries = Entry.objects.filter(recipient=profile_user)
		if request.user.username == usr:
			# viewing own profile
			return render_to_response("edit-profile.html",
								  locals(),
								  context_instance=RequestContext(request))
		else:
			# viewing someone else's profile
			return render_to_response("profile.html",
								  locals(),
								  context_instance=RequestContext(request))