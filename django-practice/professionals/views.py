from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from authentications.auth import professional_only
from .forms import ServiceForm
from .models import Servc
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.


@login_required 
@professional_only
def professionalDashboard(request):
    return render(request, 'professionals/professionalDashboard.html')


@login_required 
@professional_only
def profAddService(request):
    if request.method == 'POST':
        form=ServiceForm(request.POST)
        if form.is_valid():
            service = form.save()
            service.service_user = request.user
            service.save()
            messages.add_message(request, messages.SUCCESS, 'Service added successfully')
            return redirect('/professionals/profshowservice')
        else:
            messages.add_message(request, messages.ERROR, 'Unable to add service')
            context = {'serviceForm':form}
            return render(request, 'professionals/profAddService.html', context)
    context = {'serviceForm':ServiceForm}
    return render(request, 'professionals/profAddService.html', context)


@login_required 
@professional_only
def profShowService(request):
    user = request.user
    services = Servc.objects.filter(service_user=user)
    context = {'services':services}
    return render(request, 'professionals/profShowService.html', context)