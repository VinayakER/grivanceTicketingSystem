from django.http import HttpResponse, JsonResponse
from .models import Grievance, Comment
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
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

@login_required
def ticketDetails(request, id):
    ticket = Grievance.objects.get(id=id)
    comments = Comment.objects.filter(ticket=ticket)
    return render(request,"grievance/ticketDetails.html", context={"ticket":ticket, "comments":comments})

@login_required
def comment(request, ticket_id):
    if request.method=="POST":
        data = request.POST
        if data.get("message"):
            ticket = Grievance.objects.get(id=ticket_id)
            c = Comment(body=data.get("message"),ticket=ticket, created_by=request.user)
            c.save()
    # comment = Comment()
    return redirect(f"/ticket/{ticket_id}")


@login_required
def ticketStatus(request, ticket_id, value):

    ticket = Grievance.objects.get(id=ticket_id)
    ticket.status = value
    ticket.save()
    # comment = Comment()
    return redirect(f"/ticket/{ticket_id}")
