from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate
from .forms import Signupform
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse

def signup(request):
    if request.method=="POST":
        form=Signupform(request.POST)
        if form.is_valid():
            form.save()
            return redirect(user_login)
    else:
        form=Signupform()
    return render(request,'signup.html',{'form':form})

def Homepage(request):
    return render(request,'home.html',{})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return render(request,'home.html',{})
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'login.html', {})