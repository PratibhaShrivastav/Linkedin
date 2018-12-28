from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate,logout
from .forms import Signupform
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from .tokens import account_activation_token
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.models import User
from django.contrib import messages

def signup(request):
    if request.method=="POST":
        print("Check 1")
        form=Signupform(request.POST)
        if form.is_valid():
            print("Check 2")
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            subject = 'Activate Your MySite Account'
            message = render_to_string('account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            print(message)
            result = user.email_user(subject, message)
            print(result)
            return redirect('account_activation_sent')
        else:
            messages.warning(request,"Form has some errors: either the passwords don't match , weak password or invalid email address")
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

def logout_view(request):
    logout(request)
    return render(request,'signup.html',{})

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        #user.profile.email_confirmed = True
        user.save()
        login(request, user)
        return redirect('home')
    else:
        return render(request, 'account_activation_invalid.html')


def account_activation_sent(request):
    return render(request, 'account_activation_sent.html')