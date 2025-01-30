from django.shortcuts import render,redirect
from myApp.models import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def signupPage(request):
    
    if request.method=="POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
       
        if password1==password2:
            user = customUser.objects.create_user(username=username, password=password1) 
            
            user.email = email
            user.user_type = "1"
            
            user.save()
            messages.success(request, 'Successfully Sent The Message!')
            return redirect('signinPage') 
        
        else:
            messages.warning(request, 'Username and Password not Matched !')
            return redirect('signupPage') 
        
    return render(request,'Common/signupPage.html')




def signinPage(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username,password=password)
        
        if user is not None:
            login(request,user)
            
            if user.user_type =='1':
                messages.success(request, 'Successfully Your Are Logined !')
                return redirect('adminDashboard')
            
            elif user.user_type =='2':
                messages.success(request, 'Successfully Your Are Logined !')
                return redirect('teacherdashboard')
            
            elif user.user_type =='3':
                messages.success(request, 'Successfully Your Are Logined !')
                return redirect('studentdashboard')
            
        else:
            messages.warning(request, 'Username and Password not Matched !')
            return redirect('signinPage')
        
    return render(request,'Common/signinPage.html')


def logoutPage(request):
    logout(request)
    return redirect('signinPage')

