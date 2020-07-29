from django.shortcuts import render,redirect
from register.forms import  UserRegistration, RailwayUserForm
from .models import RegisterUser
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.

def RailwayHomePage(request):
    return render(request, 'register/home.html', {'RailwayUserList': RailwayUserList})


@login_required
def RailwayUserList(request):
    RailwayUserList = RegisterUser.objects.all()
    return render(request, 'register/userlist.html', {'RailwayUserList': RailwayUserList})


def UserRegistrationview(request):
    if request.method=='POST':
        form=UserRegistration(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get['username']
            messages.success(request,f'Account has been Created. Kindly Login')

    else:

        form= UserRegistration()
        return render(request,'register/railwayregister.html',{'form':form})


@login_required
def RailwayUserRegistrationview(request):
    Rform=RailwayUserForm()
    if request.method == 'POST':
        Rform=RailwayUserForm(request.POST)
        if Rform.is_valid:
            Rform.save()
            return redirect('list')
    return render(request,'register/railwayform.html',{'Rform':Rform})


def UserUpdate(request,id):
    register=RegisterUser.objects.get(id=id)
    if request.method=='POST':
         form=RailwayUserForm(request.POST,instance=register)
         if form.is_valid:
          form.save()
          return redirect('/list')
    return render(request,'register/update.html',{'register':register})



def UserDelete(request,id):
    register=RegisterUser.objects.get(id=id)
    register.delete()
    return redirect('/')
