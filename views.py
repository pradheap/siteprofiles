from siteprofiles.forms import StudentForm
from django.contrib.auth.models import User
from siteprofiles.models import *
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse 
from django.contrib.auth import authenticate, login
from django.template import RequestContext
from django.shortcuts import redirect
 

# Function for Editing a User Profile
def edit_profile(request):
    uname = request.user
    st = Student.objects.get(user=uname)
    if request.method == 'POST':
    	form = StudentForm(request.POST,instance=st)
    else:
    	form = StudentForm(instance=st)
    if form.is_valid():
    	form.save()
    	return redirect('/profile/detail') 
    else:
    	return render_to_response('edit_profile.html',{'form':form}, context_instance=RequestContext(request))
    	
# Function for Viewing a User Profile
def view_profile(request):
	uname = request.user
	st = Student.objects.get(user=uname)
 	return render_to_response('profile_detail.html', {'st':st}, context_instance=RequestContext(request))
  
# Separate function for Login. (May be remove it later or modify it)
def login_user(request):
    state = "Please log in below..."
    username = password = ''
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                state = "You're successfully logged in!"
                return redirect('siteprofiles.views.edit_profile') 
            else:
                state = "Your account is not active, please contact the site admin."
        else:
            state = "Your username and/or password were incorrect."
    return render_to_response('siteprofiles.views.login_user',{'state':state, 'username': username}, RequestContext(request))