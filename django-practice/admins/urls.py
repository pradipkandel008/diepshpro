from django.urls import path
from . import views 

urlpatterns = [
    path('',views.adminDashboard, name='admins'),
    path('addservice',views.addService, name='addservice'),
    path('showservice',views.showService, name='showservice'),
    path('deleteservice/<str:service_id>',views.deleteService, name='deleteservice'),
    path('updateservice/<str:service_id>',views.updateService, name='updateservice'),


]