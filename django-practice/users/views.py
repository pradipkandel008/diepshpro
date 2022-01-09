from django.core.checks import messages
from django.contrib import messages
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from authentications.auth import user_only
from authentications.forms import ProfileForm
from authentications.models import Profile



@login_required 
@user_only
def userDashboard(request):
    return render(request, 'users/userDashboard.html')

@login_required
@user_only
def userProfile(request):
    profile= request.user.profile
    if request.method == 'POST':
        userdata = ProfileForm(request.POST, request.FILES, instance=profile)
        if userdata.is_valid():
            userdata.save()
            messages.add_message(request, messages.SUCCESS, 'Profile data updated successfully!')
            return redirect('/users/userprofile')
        else:
            messages.add_message(request, messages.ERROR, "Something went wrong!")
            context={'profileForm':userdata}
            return render(request, 'users/userProfile.html',context)



    context = {'profileForm':ProfileForm(instance=profile)}
    return render(request, 'users/userProfile.html', context)



# FS/OS - file system to remove paila ko image