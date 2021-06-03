from django.shortcuts import render,redirect
from django.core.exceptions import ValidationError
from . models import User
from . backend import SettingsBackend
from django.contrib import auth,messages
def register(request):
    if request.method=="POST":
        email=request.POST['email']
        name=request.POST['name']
        pass1=request.POST['password']
        pass2=request.POST['conf-password']
        is_recruiter=request.POST['is_recruiter']
     
        if(pass1==pass2 and len(pass1)>8 and pass1.isalnum()):
            if User.objects.filter(email=email).exists():
                print('user id exists')
                messages.info(request,'User id exists')
                return redirect('register')
            else:
                user=User.objects.create_user(email=email,name=name,password=pass1,is_recruiter=is_recruiter)
                user.save()
                print('user created')
                # messages.info(request,'User Created') 
                return redirect('login')
        else:
            messages.info(request,'1.password length should be>8 | 2.both password should be same | 3.password must be alpha numeric')
            return redirect('register')
        return redirect('login')
    else:
        return render(request,'user/signup.html')


def login(request):
    if request.method=="POST":

        print(request)
        email=request.POST['email']
        password=request.POST['password']
        is_recruiter=request.POST['is_recruiter']
        user=SettingsBackend.authenticate(email=email,password=password)
        print(user,request.POST)
        if user!=None:
            auth.login(request,user)
            
            if user.is_recruiter and is_recruiter=='1':
                print("in the recruiter")
                return redirect('recruiter')
                print("recruiter logged in ")
            if (not user.is_recruiter) and is_recruiter=='0':
                return redirect('recruiter')
                print("recruiter logged in ")
            else:
                messages.info(request,'Invalid Credentials inner')
                return redirect('login')
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')
    else:
        return render(request,'user/login.html')
    

def logout(request):
    auth.logout(request)
    return redirect('login')


