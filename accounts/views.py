from django.shortcuts import render,redirect
from .forms import *
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
            login(request,user)
            return redirect('accounts:profile')
        else:
            return render(request,'error.html')
    return render(request,'accounts/login.html')

def profile(request):
    profile=Profile.objects.get(user=request.user)
    return render(request,'accounts/profile.html',{'profile':profile})

def logout_view(request):
    logout(request)
    return redirect("accounts:login_view")

def edit_profile(request):
    profile=Profile.objects.get(user=request.user)
    print('Here, ');print('There')
    if request.method=="POST":
        uForm = UserForm(request.POST,request.FILES,instance=request.user)
        pForm= ProfileForm(request.POST,request.FILES,instance=request.user)
        if uForm.is_valid() and pForm.is_valid():
            uForm.save()
            pForm.save()
        return redirect('accounts:profile')
    else:
        uForm=UserForm(instance=request.user)
        pForm=ProfileForm(instance=profile)
    context={
        'userForm':uForm,
        'profileForm':pForm,
    }
    return render(request,'accounts/edit_profile.html',context)