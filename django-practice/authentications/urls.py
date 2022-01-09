from django.urls import path
from . import views 

urlpatterns = [
    path('loginpage',views.loginPage, name='loginpage'),
    path('signup',views.signup,name='signup'),
    path('prosignup',views.proSignup,name='prosignup'),
    path('signout',views.signout,name='signout'),


]