# all_users views.py

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

from django.views.generic import TemplateView
from django.http import HttpResponse

import json

class SignUpView(TemplateView):

	template_name = 'all_users/signup.html'


def login_view(request):

	if request.method == 'POST':

		print("Am I in here yet?")
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)

		response_data = {}

		if user is not None:
			login(request, user)
			response_data['result'] = 'success'
		else:
			response_data['result'] = 'failed'
			response_data['message'] = 'Username or password incorrect'

	return HttpResponse(
		json.dumps(response_data),
		content_type='application/json',
		status=201)

