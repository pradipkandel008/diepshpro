from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from authentications.auth import admin_only
from .forms import ServiceForm
from .models import Service
from django.contrib import messages

# Create your views here.


@login_required 
@admin_only
def adminDashboard(request):
    return render(request, 'admins/adminDashboard.html')


@login_required 
@admin_only
def addService(request):
    if request.method=='POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS , 'Service added successfully!')
            return redirect('/admins/showservice')
        else:
            messages.add_message(request, messages.ERROR, 'Please verify the form fields.')
            context = {'serviceForm':form}
            return render(request, 'admins/addService.html',context)

    context = {'serviceForm':ServiceForm}
    return render(request, 'admins/addService.html',context)


@login_required 
@admin_only
def showService(request):
    services =  Service.objects.all()
    context = {'services':services}
    return render(request, 'admins/showService.html',context)



@login_required 
@admin_only
def deleteService(request, service_id):
    service = Service.objects.get(id=service_id)
    service.delete()
    messages.add_message(request, messages.SUCCESS, 'Service Deleted Successfully!')
    return redirect('/admins/showservice')

@login_required 
@admin_only
def updateService(request, service_id):
    service = Service.objects.get(id=service_id)
    if request.method =='POST':
        form = ServiceForm(request.POST, instance=service)
        if form.is_valid:
            form.save()
            messages.add_message(request,messages.SUCCESS,'Service Data Updated Successfully!')
            return redirect('/admins/showservice')
        else:
            messages.add_message(request, messages.ERROR, 'Please verify the form fields.')
            context = {'serviceUpdateForm':form}
            return render(request, 'admins/updateService.html',context)
        
    context = {'serviceUpdateForm':ServiceForm(instance=service)}
    return render(request, 'admins/updateService.html', context)
