from django.urls import path
from . import views 

urlpatterns = [
    path('',views.professionalDashboard, name='professionals'),
    path('profaddservice',views.profAddService, name='profaddservice'),
    path('profshowservice',views.profShowService, name='profshowservice'),



]