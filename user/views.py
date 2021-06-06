from django.shortcuts import render,redirect
from django.core.exceptions import ValidationError
from . models import User
from . backend import SettingsBackend
from django.contrib import auth,messages

#View for registration of new user
def register(request):
    if request.method=="POST":
        email=request.POST['email']
        name=request.POST['name']
        pass1=request.POST['password']
        pass2=request.POST['conf-password']
        if request.POST['is_recruiter']=='1':
            is_recruiter=True
        else:
            is_recruiter=False
        if(pass1==pass2 and len(pass1)>8):
            if User.objects.filter(email=email).exists():
                messages.info(request,'User with this email already exists')
                return redirect('register')
            else:
                user=User.objects.create_user(email=email,password=pass1)
                user.name=name
                user.is_recruiter=is_recruiter
                user.save()
                return redirect('login')
        else:
            messages.info(request,'Make sure both passwords are same and length of password > 8')
            return redirect('register')
        return redirect('login')
    else:
        return render(request,'user/signup.html')

#View for user login
def login(request):
    if request.method=="POST":
        email=request.POST.get('email')
        password=request.POST.get('password')
        is_recruiter=request.POST['is_recruiter']
        user=SettingsBackend.authenticate(email=email,password=password)
        if user!=None:
            auth.login(request,user)
            if user.is_recruiter and is_recruiter=='1':
                return redirect('recruiter')
            if (not user.is_recruiter) and is_recruiter=='0':
                return redirect('student')
            else:
                messages.info(request,'Invalid Credentials')
                return redirect('login')
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')
    else:
        return render(request,'user/login.html')
    
#View for user logout 
def logout(request):
    auth.logout(request)
    return redirect('login')


