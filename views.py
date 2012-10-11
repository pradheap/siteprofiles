from siteprofiles.forms import ProfileForm
from django.contrib.auth.models import User
from siteprofiles.models import *
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse 
from django.contrib.auth import authenticate, login
from django.template import RequestContext
 

def edit_profile(request):
	def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        try:
            self.fields['email'].initial = self.instance.user.email

	form = ProfileForm()
	if request.method == 'POST': # If the form has been submitted...
	  	u = request.user
		st = Student.objects.get(user=u)
		form = ProfileForm(request.POST) # A form bound to the POST data
        if form.is_valid():
	        """
	        Update the primary email address on the related User object as well.
	        """
	        st.first_name =  form.cleaned_data['first_name'] 
	        st.last_name =  form.cleaned_data['last_name']
	        #st.reg_no =  form.cleaned_data['reg_no']
	        st.save()
	        #u.email = self.cleaned_data['email']
	        #u.save()
	        #profile = super(ProfileForm, self).save(*args,**kwargs)
	        return HttpResponseRedirect('/profile/detail')
   	else:
   	    u = request.user
   	    #st = Student.objects.get(user=u)
   	    form = ProfileForm()
   	#backend.EditProfile(request, **kwargs)
   	return render_to_response('edit_profile.html',{'form':form}, context_instance=RequestContext(request))

#def create_profile(request):
 # return profile_views.create_profile(request, form_class=ProfileForm)
  
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
            else:
                state = "Your account is not active, please contact the site admin."
        else:
            state = "Your username and/or password were incorrect."

    return render_to_response('profile.html',{'state':state, 'username': username}, RequestContext(request))