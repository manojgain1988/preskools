from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required




@login_required
def adminDashboard(request):
    context = {}
    return render(request,'myAdmin/admindashboard.html',context)
 
 
@login_required
def teacherdashboard(request):
    context = {}
    return render(request,'Teacher/teacherdashboard.html',context)
 
@login_required
def teacherlist(request):
    context = {}
    return render(request,'Teacher/teacherlist.html',context)
 
@login_required
def teacheradd(request):
    context = {}
    return render(request,'Teacher/teacheradd.html',context)
 
 
@login_required
def teacherview(request):
    context = {}
    return render(request,'Teacher/teacherview.html',context)
 
@login_required
def teacheredit(request):
    context = {}
    return render(request,'Teacher/teacheredit.html',context)
 

@login_required
def studentdashboard(request):
    context = {}
    return render(request,'Student/studentdashboard.html',context)
 
@login_required
def studentlist(request):
    context = {}
    return render(request,'Student/studentlist.html',context)
 
@login_required
def studentview(request):
    context = {}
    return render(request,'Student/studentview.html',context)
 
 
@login_required
def studentadd(request):
    context = {}
    return render(request,'Student/studentadd.html',context)
 
@login_required
def studentedit(request):
    context = {}
    return render(request,'Student/studentedit.html',context)
 
 
@login_required
def departmentlist(request):
    context = {}
    return render(request,'Department/departmentlist.html',context)
 
 
@login_required
def departmentadd(request):
    context = {}
    return render(request,'Department/departmentadd.html',context)
 
@login_required
def departmentview(request):
    context = {}
    return render(request,'Department/departmentview.html',context)
 
@login_required
def subjectlist(request): 
    context = {}
    return render(request,'Subject/subjectlist.html',context)
 
 
@login_required
def subjectadd(request):
    context = {}
    return render(request,'Subject/subjectadd.html',context)
 
@login_required
def subjectedit(request):
    context = {}
    return render(request,'Subject/subjectedit.html',context)
 
