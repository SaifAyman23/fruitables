from django.shortcuts import render,redirect
from .forms import *
from shop.models import Order
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def register(request):
    if request.method=='POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            user=authenticate(username=username,password=password)
            login(request,user)
            return redirect("accounts:profile")
    context={
        'form':RegisterForm()
    }
    return render(request,"accounts/register.html",context)

def login_view(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        if username and password:
            user=authenticate(username=username,password=password)
            if user:
                login(request,user)
                return redirect('accounts:profile')
            else:
                return render(request,'error.html')
        else:
            return render(request,'error.html')
    return render(request,'accounts/login.html')

def profile(request,order=None):
    profile=Profile.objects.get(user=request.user)
    try:
        order=Order.objects.all().filter(user=request.user)
    except:
        pass
    context={
        'profile':profile,
        'order':order,
    }
    return render(request,'accounts/profile.html',context)

def logout_view(request):
    logout(request)
    return redirect("accounts:login_view")

def edit_profile(request):
    profile=Profile.objects.get(user=request.user)
    if request.method=="POST":
        uForm = UserForm(request.POST,request.FILES,instance=request.user)
        pForm= ProfileForm(request.POST,request.FILES,instance=profile)
        if uForm.is_valid() and pForm.is_valid():
            uForm.save()
            pForm.save()
            return redirect('accounts:profile')
        else:
            return render(request,'error.html')
    else:
        uForm=UserForm(instance=request.user)
        pForm=ProfileForm(instance=profile)
    context={
        'userForm':uForm,
        'profileForm':pForm,
    }
    return render(request,'accounts/edit_profile.html',context)

def reset_password(request):
    if request.method=='POST':
        user=request.user
        username=request.POST['username']
        password=request.POST['password']
        new_password=request.POST['new_password']
        user=authenticate(username=username,password=password)
        if user:
            user.set_password(new_password)
            user.save()
            login(request,user)
            return redirect('accounts:profile')
                
    return render(request,'accounts/reset_password.html')