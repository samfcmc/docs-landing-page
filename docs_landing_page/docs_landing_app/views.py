from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout

import fenixedu
from fenixedu.authentication import users

config = fenixedu.FenixEduConfiguration.fromConfigFile()
client = fenixedu.FenixEduClient(config)

# Create your views here.
def index(request):
	context = {'auth_url': client.get_authentication_url()}
	code = request.GET.get('code', None)

	if code is not None and not request.user.is_authenticated():
		user = authenticate(request=request, client=client, code=code)
		if user is not None:
			login(request, user)
			user = users.get_fenixedu_user(request)
			person = client.get_person(user=user)
			request.session['photo'] = person['photo']['data']

	return render(request, 'index.html', context)

def user_logout(request):
	logout(request)
	return redirect('index')
