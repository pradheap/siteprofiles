from siteprofiles.forms import *
from django.contrib.auth.models import User
from django.forms.models import inlineformset_factory
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

	CollegeFormSet = inlineformset_factory(Student,Education, extra=0,can_delete=False)
	uname = request.user
	st = Student.objects.get(user=uname)
	addr = st.address
	if request.method == 'POST':
		form = StudentForm(request.POST,instance=st)
		addr_form = AddressForm(request.POST, instance=addr)
		if 'add_college' in request.POST:
			cp = request.POST.copy()
			cp['college-TOTAL_FORMS'] = int(cp['college-TOTAL_FORMS'])+ 1
			new_college = CollegeFormSet(cp,prefix='college',instance=st)
		elif 'submit' in request.POST:
			if addr_form.is_valid():
				addr = addr_form.save()
			if form.is_valid():
				st = form.save(commit=False)
				st.address = addr
				st.save()
				new_college = CollegeFormSet(request.POST,prefix='college',instance=st)
			if new_college.is_valid():
				new_college.save()
				return redirect('/profile/detail') 
	else:
		form = StudentForm(instance=st)
		addr_form = AddressForm(instance=addr)
		new_college = CollegeFormSet(prefix='college',instance=st)
	return render_to_response('edit_profile.html',{'form':form,'addr_form':addr_form,'college':new_college }, context_instance=RequestContext(request))
    	
# Function for Viewing a User Profile
def view_profile(request):
	uname = request.user
	st = Student.objects.get(user=uname)
	addr = st.address
	edu = Education.objects.get(student=st)
 	return render_to_response('profile_detail.html', {'st':st,'addr':addr,'edu':edu}, context_instance=RequestContext(request))
  
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
                return redirect('siteprofiles.views.view_profile') 
            else:
                state = "Your account is not active, please contact the site admin."
        else:
            state = "Your username and/or password were incorrect."
    return render_to_response('siteprofiles.views.login_user',{'state':state, 'username': username}, RequestContext(request))