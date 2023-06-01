from django.http import HttpResponse
from .models import Grievance
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def grievance(request):
    grievances=Grievance.objects.all()
    

    return render(request,'grievance/grievance.html',context={'grievances':grievances})
@login_required
def make_complaint(request):
    if not request.user.is_student:
        messages.error(request, 'You are not allowed to create new Grievance')
        return redirect("/")

    if request.method=='POST':
        data=request.POST
        grievance=Grievance(title=data['title'],description=data['description'],created_by=request.user,)
        grievance.save()
        messages.success(request, f'Grievance with Ref.id {grievance.id} created successfully')
        return redirect("/")

    return render(request,'grievance/make_complaint.html')