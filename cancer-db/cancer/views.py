# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.core.context_processors import csrf
from django.core.urlresolvers import reverse
from django.shortcuts import render, render_to_response, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

import sys
import logging

logr = logging.getLogger(__name__)


#auth_view
def login_view(request):
	
	if request.POST:
		args = {}
		args.update(csrf(request))	
		has_error = False
		user_id = request.POST.get('username')#'mah29'
		passwd = request.POST.get('password')#'mhdPfizer1384'
		args['user_id'] = user_id	
		if not user_id:
			has_error = True
			args['user_id_error'] = '用户名不能为空'

		if not passwd:
						has_error = True
						args['passwd_error'] = '密码不能为空'

		user = authenticate(username=user_id, password=passwd)
		
		if not user:
				has_error = True
				args['validate_error'] = '无法确认您的用户名密码，请确认输入正确'	

		if has_error:
			return render(request,'login.html',args)	
		else:
			if user.is_active:
				login(request, user)
				#authenticate user
				return HttpResponseRedirect('/dashboard/')
			else:
				# Return a 'disabled account' error message
				return HttpResponseRedirect('/')
	
	else:
		if request.user.is_authenticated():
			return HttpResponseRedirect('/dashboard/')	
		else:
			return render(request,'login.html')


def loggedin(request):
	return render_to_response('loggedin.html', 
							  {'full_name': request.user.username})

def logout_view(request):
	logout(request)
	return HttpResponseRedirect("/")

def logout_success(request):
	return render_to_response('logout.html')


def register_user(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/accounts/register_success')
		
	else:
		form = UserCreationForm()
	args = {}
	args.update(csrf(request))
	
	args['form'] = form
	
	return render_to_response('register.html', args)



def register_success(request):
	return render_to_response('register_success.html')

def help(request):

	return render_to_response('help.html')

'''
def contact(request):
    if request.method == 'POST':
	form = ContactForm(request.POST)
	if form.is_valid():        
	  	fromemail = form.cleaned_data['from_email']
		header = form.cleaned_data['subject']
		to =  DEFAULT_ADMIN_EMAIL_LIST
		content = form.cleaned_data['content']
		msg = EmailMultiAlternatives(header, content, fromemail, to)
		msg.content_subtype = "html"
		msg.send()

		return HttpResponseRedirect('/dashboard/confirm/?h=success&t=Email Sent!&c=We will try to come back to you ASAP! &b1=main&b2=console')
    else:

	if request.user.is_authenticated():
		init_data = {'from_email':request.user.email}
                form = ContactForm(initial=init_data)
	else:
        	form = ContactForm()

    args = {}
    args.update(csrf(request))
    args['contactform'] = form
    args['user'] = request.user

    return render_to_response('contact_form.html', args)
'''

