from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import ProfileModel
from .forms import *
from django.contrib.auth.decorators import login_required


def sign_up(request):
    if request.method=="POST":
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']

        usr=User(username=username,email=email)
        usr.set_password(password)
        usr.save()
        count = User.objects.filter(username=username,email=email,password=password).count()
        if count>0:
            request.session['login']=True
        return redirect("login")

    return render(request,"sign_up.html")
    
def loginview(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']

        usr=authenticate(username=username,password=password)
        if usr:
            login(request,usr)
            return redirect("index")
    return render(request,"login.html")


@login_required
def logoutview(request):
    logout(request)
    # return redirect("index")
    return render(request,"logout.html")
@login_required
def profile(request):
    data = ProfileModel.objects.filter(user=request.user).all()

    if request.method=="POST" :
        u_form=UserUpdateForm(request.POST or None,instance=request.user)
        p_form=ProfileUpdateForm(request.POST or None, request.FILES or None  ,instance=request.user.profilemodel)
        if u_form.is_valid() and p_form.is_valid():
            print("VALID")
            u_form.save()
            p_form.save()
            return redirect("profile")
        else:
            print(u_form.errors,">>>>>>>>>",p_form.errors)
    else:
        u_form=UserUpdateForm(instance=request.user)
        p_form=ProfileUpdateForm(instance=request.user.profilemodel)

    context={
        'u_form':u_form,'p_form':p_form,'data':data
        
    }
    return render(request,"profile.html",context)
    
