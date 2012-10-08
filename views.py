from siteprofiles.forms import ProfileForm, 
from django.contrib.auth.models import User
from siteProfiles.models import UserProfile
from django.core.exceptions import ObjectDoesNotExist
 
def edit_profile(request):
  return profile_views.edit_profile(request, form_class=ProfileForm)
