from django.contrib.messages.api import success
from django.http import request
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import CreateUserForm
from .auth import unauthenticated_user
from .models import Profile

# Create your views here.

@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            if user.is_superuser and user.is_staff:
                return redirect('/admins')
            elif not user.is_superuser and not user.is_staff:
                return redirect('/users')
            elif not user.is_superuser and user.is_staff:
                return redirect('/professionals')

        elif user is None:
            messages.add_message(request, messages.ERROR, 'Please provide correct credentials')
    return render(request, "authentications/login.html")




    # return render(request, 'authentications/login.html')

@unauthenticated_user
def signup(request):

    if request.method=='POST':
        userdata = CreateUserForm(request.POST)
        if userdata.is_valid():
            user = userdata.save()

            Profile.objects.create(user=user, username=user.username, email= user.email) 

            # user.is_staff = True  # This is for professional user registration
            # user.save()
            messages.add_message(request, messages.SUCCESS, 'User registered successfully!' )
            return redirect('/auth/loginpage')
        else:
            context = {'form' : userdata}
            messages.add_message(request, messages.ERROR, 'Bad Credentials!' )

            return render(request, 'authentications/signup.html',context)


    context ={'form' : CreateUserForm}
    return render(request, 'authentications/signup.html', context)


@unauthenticated_user
def proSignup(request):

    if request.method=='POST':
        userdata = CreateUserForm(request.POST)
        if userdata.is_valid():
            user = userdata.save()

            Profile.objects.create(user=user, username=user.username, email= user.email) 

            user.is_staff = True
            # This is for professional user registration
            user.save()
            messages.add_message(request, messages.SUCCESS, 'Successfully Signed Up as Professional!' )
            return redirect('/auth/loginpage')
        else:
            context = {'form' : userdata}
            messages.add_message(request, messages.ERROR, 'Bad Credentials!' )

            return render(request, 'authentications/signup.html',context)


    context ={'form' : CreateUserForm}
    return render(request, 'authentications/signup.html', context)





def signout(request):
    logout(request)
    return redirect('/auth/loginpage')






    # return render(request, 'authentications/signup.html')
    