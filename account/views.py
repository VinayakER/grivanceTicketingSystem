from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth import login, authenticate ,logout
from django.contrib.auth.decorators import login_required
from grievance.models import Grievance

from django.contrib import messages

def loginOptionPage(request):
    if request.user.is_authenticated:
        return redirect('/')
    return render(request,'account/login_option.html')

def userLogin(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method=="POST":
        data=request.POST
        username=data.get('username')
        password=data.get('password')
        user=authenticate(username=username,password=password)
        if user:
            if not user.is_student:
                messages.error(request, 'Invalid username or passoword for student')
                return render(request,'account/user.html')
            login(request,user)
            return redirect('/')
        else:
            messages.error(request, 'Invalid username or passoword')
        
    return render(request,'account/user.html')

def adminLogin(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method=="POST":
        data=request.POST
        username=data.get('username')
        password=data.get('password')
        user=authenticate(username=username,password=password)
        if user:
            if not (user.is_admin or user.is_staff):
                messages.error(request, 'Invalid username or passoword for admin')
                return render(request,'account/admin.html')
            login(request,user)
            return redirect('/')
        else:
            messages.error(request, 'Invalid username or passoword')


    return render(request,'account/admin.html')
def logoutView(request):
    logout(request)
    return redirect('/login')
@login_required
def dashboard(request):
    user=request.user
    status = request.GET.get("status")
    if (user.is_student or user.is_admin or user.is_staff):
        if user.is_student:
            grievances=Grievance.objects.filter(created_by=user)
            context={
                "grievances":grievances
            }
        else:
            if status and (status in [1,2,3,4,"1","2","3","4"]):
                if user.is_staff:
                    grievances=Grievance.objects.filter(status=status, assigned_to=user)
                else:
                    grievances=Grievance.objects.filter(status=status)

            else:
                if user.is_staff:
                    grievances=Grievance.objects.filter(assigned_to=user)
                
                else:
                    grievances=Grievance.objects.all()
            
            if user.is_staff:
                new_count=Grievance.objects.filter(assigned_to=user,status=1).count()
                open_count=Grievance.objects.filter(assigned_to=user,status=2).count()
                resolved_count=Grievance.objects.filter(assigned_to=user,status=3).count()
                closed_count=Grievance.objects.filter(assigned_to=user,status=4).count()
            else:
                new_count=Grievance.objects.filter(status=1).count()
                open_count=Grievance.objects.filter(status=2).count()
                resolved_count=Grievance.objects.filter(status=3).count()
                closed_count=Grievance.objects.filter(status=4).count()
            
            
            context={
                'grievances':grievances,
                'new_count':new_count,
                'open_count':open_count,
                'resolved_count':resolved_count,
                'closed_count':closed_count,
                }

        return render(request,'account/user_dashboard.html',context=context)

    return HttpResponse(f"Sorry {user.username}, you are not allowed to access this page")


def admin_dashboard(request):
    admin=request.admin
    if(admin.is_admin):
        grievances=Grievance.objects.all()
        return render(request,'account/admin_dahboard.html',context={'grievances':grievances})