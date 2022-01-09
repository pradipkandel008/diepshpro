from django.urls import path
from . import views 

urlpatterns = [
    path('',views.userDashboard, name='users'),
    path('userprofile',views.userProfile, name='userprofile'),



]